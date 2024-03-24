from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import stripe
import json


stripe.api_key = 'sk_test_51OvdMP05WaGaUN1tfmtSLPQrykPzGg2xpQjxb4ydWmnEYAIjK21lSaHiG15ipO2LmmFIDtdY8tmQCq7JaxWo0VVg00616eekOQ'

DOMAIN = 'http://localhost:8080' #ご自身のドメインを設定

def create_checkout_session(request):

    try:
        prices = stripe.Price.list(
            lookup_keys=[request.POST['lookup_key']], 
            expand=['data.product']
        )
        checkout_session = stripe.checkout.Session.create(
            # client_reference_id = ＜user_idなどユーザ識別子＞,  #自サーバ⇔Stripe間のユーザ紐づけのため
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
    
    
def customer_portal():
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


# Replace this endpoint secret with your endpoint's unique secret
# If you are testing with the CLI, find the secret by running 'stripe listen'
# If you are using an endpoint defined with the API or dashboard, look in your webhook settings
# at https://dashboard.stripe.com/webhooks



def webhook():
    event = None
    payload = request.data

    try:
        event = json.loads(payload)
    except json.decoder.JSONDecodeError as e:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return jsonify(success=False)
    if endpoint_secret:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return jsonify(success=False)

    # Handle the event
    if event and event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']  # contains a stripe.PaymentIntent
        print('Payment for {} succeeded'.format(payment_intent['amount']))
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
    elif event['type'] == 'payment_method.attached':
        payment_method = event['data']['object']  # contains a stripe.PaymentMethod
        # Then define and call a method to handle the successful attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
    else:
        # Unexpected event type
        print('Unhandled event type {}'.format(event['type']))

    return jsonify(success=True)