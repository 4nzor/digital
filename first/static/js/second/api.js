function control(command, id) {
    $('#'+id).fadeOut();
    const csrf_token = getCookie('csrftoken');
    $.ajax({
        url: '/database/control/',
        type: 'POST',
        data: {'csrfmiddlewaretoken': csrf_token, 'command': command, 'id': id}

    })

}



