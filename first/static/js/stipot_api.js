function get_platform(value, url) {
    token = '{{csrf_token}}';
    jQuery.ajax({
        type: 'POST',
        url: url,
        data: {'csrfmiddlewaretoken': token, 'country': value},

        success: function (data) {
            options = "";
            for (var i = 0; i < data.platforms.length; i++) {
                options += "<option>" + data.platforms[i] + "</option>";
            }
            $("#async_platform").html(options);

        }
    })
}


function get_apps(url, token) {
    // noinspection JSAnnotator
    let type = $('.lectures_active').text();
    let date = $('#yourId3 input.data1').val();
    if (date)
        pass = 1;
    else {
        today = new Date();
        let dd = today.getDate();
        let mm = today.getMonth() + 1;
        let yyyy = today.getFullYear();
        if (dd < 10) {
            dd = '0' + dd
        }

        if (mm < 10) {
            mm = '0' + mm
        }
        date = yyyy + '-' + mm + '-' + dd;

    }

    jQuery.ajax({
        type: 'POST',
        url: url,
        data: {
            'csrfmiddlewaretoken': token,
            'date': date,
            'type_command': type
        },
        success: function (data) {

            dat = '';
            for (let i = 0; i < data.date.length; i++) {
                dat += '<div class="lectures_block_lecture">'+'<div class="lectures_date_lecture">' +
                    data.date[i] + '</div>' + '<div class="lectures_name_lecture">' + data.titles[i] + '</div>' + '</div>';
            }
            $('.planned_lectures').html(dat);
            $('.complended_lectures').html(dat);
            $('.canceled_lectures').html(dat);
        }

    });
}




