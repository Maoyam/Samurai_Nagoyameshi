def create_checkout_session(request):
    YOUR_DOMAIN = 'http://127.0.0.1:8000/'  #ご自身のドメインを設定
    try:
        prices = stripe.Price.list(
            lookup_keys=[request.POST['lookup_key']],  #POSTからlookup_keyを取得しているため変更。ここで明示的に指定でもアリかと。
            expand=['data.product']
        )
        checkout_session = stripe.checkout.Session.create(
            client_reference_id = ＜user_idなどユーザ識別子＞,  #自サーバ⇔Stripe間のユーザ紐づけのため
            line_items=[
                {
                    'price': prices.data[0].id,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN +
            '＜successページのURL＞?session_id={CHECKOUT_SESSION_ID}',  #サクセスページURL
            cancel_url=YOUR_DOMAIN + '＜キャンセルページのURL＞',        #キャンセルページURL
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
