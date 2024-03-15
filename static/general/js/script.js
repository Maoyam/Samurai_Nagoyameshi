$(function () {
    // カルーセル
   $('.carousel').slick({
    autoplay: true,
    dots: true,
    infinite: true,
    autoplaySpeed: 5000,
    arrows: false,
  });

   // お気に入りボタンのクリック処理
   $(function () {
    // お気に入りボタンのクリック処理
    $('.favorite-button').on('click', function (e) {
        e.preventDefault(); // デフォルトのクリックイベントをキャンセル
        let restaurantId = $(this).data('restaurant-id'); // お気に入りに追加する店舗のIDを取得
        let button = $(this); // ボタン要素をキャッシュ

        // AJAXリクエストを使用してお気に入りを切り替える
        $.ajax({
            type: 'POST',
            url: '/toggle_favorite/' + restaurantId + '/', // お気に入りボタンのURL
            data: {
                'csrfmiddlewaretoken': '{{ csrf_token }}', // CSRFトークンを送信
            },
            success: function (response) {
                // ボタンの表示を切り替える
                button.toggleClass('active');
            },
            error: function (xhr, status, error) {
                // エラー処理
                console.error(xhr.responseText);
            }
        });
    });
});
});