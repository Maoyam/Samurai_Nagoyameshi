//  csrf_token 取得
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

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
        const csrf_token = getCookie("csrftoken");
        const isFavorite = $(this).data('favorite') === 'true'; 
        const restaurantId = $(this).data('restaurantId'); 
        const url = `/favorite_toggle/${restaurantId}/`;

        $.ajax({
            url: url,
            type: 'POST',

            contentType: "application/json",
            // 送信前にヘッダにcsrf_tokenを付与。
            beforeSend: function(xhr, settings) {
                 if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                     xhr.setRequestHeader("X-CSRFToken", csrf_token);
                 }
             },

            success: function (data) {
                if (data.status === 'success') {
                    // お気に入りの状態をトグルするためのロジック
                    $(this).data('favorite', String(!isFavorite)); 
                    if (isFavorite) {
                        $(this).html('<img src="/static/general/images/favorite_on.png" style="width: 20px; height: 20px;">');
                    } else {
                        $(this).html('<img src="/static/general/images/favorite_off.png" style="width: 20px; height: 20px;">');
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