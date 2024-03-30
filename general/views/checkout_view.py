from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import stripe
import json

class UpgradeCheckOutView(TemplateView):
    template_name = "general/upgrade_checkout.html"

class UpgradeSuccessView(TemplateView):
    template_name = "general/upgrade_success.html"

class UpgradeCancelView(TemplateView):
    template_name = "general/upgrade_cancel.html"



stripe.api_key = 'sk_test_51OvdMP05WaGaUN1tfmtSLPQrykPzGg2xpQjxb4ydWmnEYAIjK21lSaHiG15ipO2LmmFIDtdY8tmQCq7JaxWo0VVg00616eekOQ'

#ドメインを設定
DOMAIN = 'http://localhost:8000' 


def create_checkout_session(request):

    try:
        prices = stripe.Price.list(
            lookup_keys=[request.POST['lookup_key']], 
            expand=['data.product']
        )
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            #自サーバ⇔Stripe間のユーザ紐づけ
            client_reference_id = request.user.id,  
            line_items=[
                {
                    'price': prices.data[0].id,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=DOMAIN +
            '/payment_success.html?session_id={CHECKOUT_SESSION_ID}',  
            cancel_url=DOMAIN + '/cancel.html',       
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(e)
        return "Server error", 500
     
def customer_portal(request):
    # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    # Typically this is stored alongside the authenticated user in your database.
    checkout_session_id = request.POST.get('session_id')
    checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

    # This is the URL to which the customer will be redirected after they are
    # done managing their billing with the portal.
    return_url = DOMAIN

    portalSession = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=return_url,
    )
    return redirect(portalSession.url, code=303)


