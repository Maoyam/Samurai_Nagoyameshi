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
    $('#favorite-button').click(function () {
        const isFavorite = $(this).data('favorite') === 'true'; 
        const restaurantId = $(this).data('restaurantId'); 

        const url = `/favorite_toggle/${restaurantId}`;

        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
            },
            success: function (data) {
                if (data.status === 'success') {
                    // お気に入りの状態をトグルするためのロジック
                    $(this).data('favorite', String(!isFavorite)); // 文字列に変換してから反転
                    if (isFavorite) {
                        $(this).html('<img src="/static/general/images/favorite_border_black_24dp.svg" style="width: 15px; height: 15px;"> お気に入りに追加');
                    } else {
                        $(this).html('<img src="/static/general/images/favorite_black_24dp.svg" style="width: 15px; height: 15px;"> お気に入りを解除');
                    }
                } else {
                    alert(data.message);
                }
            }.bind(this),
            error: function (xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
