from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.conf import settings
from commondb.models.upgrade import StripeCustomer
from commondb.models.user import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse, HttpResponse 
import stripe

import json



#-----サブスクメソッド------


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':

        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'payment_successful?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'payment_cancelled/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body.decode('utf-8')
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    # if event['type'] == 'checkout.session.completed':

    # # jsondataをフォルダ内に書き込みするテスト  ※webhook使用時   
    if event['type'] == 'invoice.created':
        with open("request.json", mode='w') as f:
            f.write(str(event))

        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')
        print(client_reference_id)
        print(stripe_customer_id)
        print(stripe_subscription_id)
        # Get the user and create a new Stripe_Customer
 
        user = get_user_model().objects.get(id=client_reference_id)
        print(client_reference_id)
        print(user)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        print("usercreate")

        print (' just subscribed.')

    return HttpResponse(status=200)

#--------------------------------

@method_decorator(login_required,name="dispatch")
class UpgradeView(TemplateView):
    template_name = "general/user_upgrade.html"

@method_decorator(login_required,name="dispatch")
class UpgradeCheckoutView(TemplateView):
    template_name = "general/upgrade_checkout.html"
    model = StripeCustomer

@method_decorator(login_required,name="dispatch")
class UpgradeSuccessView(TemplateView):
    template_name = "general/upgrade_success.html"

@method_decorator(login_required,name="dispatch")
class UpgradeCancelView(TemplateView):
    template_name = "general/upgrade_cancel.html"




# stripe.api_key = 'sk_test_51OvdMP05WaGaUN1tfmtSLPQrykPzGg2xpQjxb4ydWmnEYAIjK21lSaHiG15ipO2LmmFIDtdY8tmQCq7JaxWo0VVg00616eekOQ'

# ドメインを設定
# DOMAIN = 'http://localhost:8000' 


# def create_checkout_session(request):
#     try:
#         prices = stripe.Price.list(
#             lookup_keys=[request.POST['lookup_key']], 
#             expand=['data.product']
#         )
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             #自サーバ⇔Stripe間のユーザ紐づけ
#             client_reference_id = request.user.id,  
#             line_items=[
#                 {
#                     'price': prices.data[0].id,
#                     'quantity': 1,
#                 },
#             ],
#             mode='subscription',
#             success_url=DOMAIN +
#             '/payment_success.html?session_id={CHECKOUT_SESSION_ID}',  
#             cancel_url=DOMAIN + '/cancel.html',       
#         )
#         return redirect(checkout_session.url, code=303)
#     except Exception as e:
#         print(e)
#         return "Server error", 500
     



