# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.conf import settings
# import stripe


# @login_required(login_url='login')
# def upgrade_page(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
#     if request.method == 'POST':
#         checkout_session = stripe.chechout.Session.create(
#             payment_method_types = ['card'],
#             line_items = [
#                 {
#                     'price': settings.PRODECT_PRICE,
#                     'quantity': 1,
                    
#                 },
#             ],
#             mode = 'payment',
#             customer_creation = 'always',
#             success_url = settings.REDIRECT_DOMAIN + '/
#                 payment_successful?session_id={CHECKOUT_SESSION_ID}'
#             cancel_url = settings.REDIRECT_DOMAIN + '/payment_cancelled',
#         )
#         return redirect(checkout_session.url, code=303)
#     return render(request, 'general/mypage.html')

# def payment_successful(request):
#     stripe.api_key = settings.STRIPE_SECRET