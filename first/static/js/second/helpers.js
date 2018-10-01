function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function hide_input(name) {

    console.log(document.getElementsByName(name)[0].hidden = true);
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: '/database/hide_input/',
        data: {'name': name, 'csrfmiddlewaretoken': csrftoken},
        success: function (data) {




        }


    })

}