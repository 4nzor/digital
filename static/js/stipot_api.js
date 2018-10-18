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
                dat += '<div class="lectures_block_lecture">' + '<div class="lectures_date_lecture">' +
                    data.date[i] + '</div>' + '<div class="lectures_name_lecture">' + data.titles[i] + '</div>' + '</div>';
            }

            $('.planned_lectures').html(dat);
            $('.complended_lectures').html(dat);
            $('.canceled_lectures').html(dat);
            let map2 = new google.maps.Map(document.getElementById('map2'),
                {
                    zoom: 6,
                    center: {
                        lat: parseFloat(data.cords[0].lat),
                        lng: parseFloat(data.cords[0].lng)
                    }

                });

            for (i = 0; i < data.cords.length; i++) {
                console.log(data.cords[i]);
                let lat = parseFloat(data.cords[i].lat);
                let lng = parseFloat(data.cords[i].lng);


                let LatLng = {lat: lat, lng: lng};
                let marker = new google.maps.Marker({
                    animation: google.maps.Animation.DROP,
                    position: LatLng,
                    map: map2,
                    icon: 'https://habrastorage.org/webt/ml/ye/dd/mlyeddoapn8ynunspbtaw4ga7mi.png',
                    label: data.cords[i].name,
                });
                markers.push(marker)


            }

        }

    });
}


function check_user(user) {
    token = '{{csrf_token}}';

    jQuery.ajax({
            type: 'POST',
            url: '/api/v1/check_user/',
            data: {
                'csrfmiddlewaretoken': token,
                'user': user
            },
            success: function (data) {

                if (data.data === 'reg_error')
                    $('.block_erorr_sign_in').css('display', 'block')
            }

        }
    )
}


function more_platf(id) {
    $.ajax({
            type: 'GET',
            url: '/api/v1/more_platf/' + id + '/',
            success: function (data) {
                let map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 15,

                });
                let contentString = '';
                for (let j = 0; j < data.titles_list.length; j++) {
                    contentString += '<p class="text_profile">' + 'Title: ' + data.titles_list[j].app__lecture_title + '</p>' +
                        '<p class="text_map_lectures">' + 'Lecture: ' + data.titles_list[j].app__user__full_name + '</p>'


                }
                map.setCenter({lat: data.lat, lng: data.lng});
                jQuery.ajax({
                    type: 'GET',
                    url: '/api/v1/eventmap/',
                    success: function (data) {

                        for (i = 0; i < data.event_coords.length; i++) {
                            console.log(data.event_coords[i]);
                            let lat = parseFloat(data.event_coords[i].lat);
                            let lng = parseFloat(data.event_coords[i].lng);
                            let LatLng = {lat: lat, lng: lng};
                            let marker = new google.maps.Marker({
                                animation: google.maps.Animation.DROP,
                                position: LatLng,
                                map: map,
                                title: 'Click to info',
                                icon: 'https://habrastorage.org/webt/ki/ru/nw/kirunwnagzq2tnrgxcaqaktv9ia.png'

                            });


                            let infowindow = new google.maps.InfoWindow({
                                content: contentString
                            });
                            markers.push(marker);
                            marker.addListener('click', function () {
                                infowindow.open(map, marker);
                            });


                        }
                    }

                });


            }
        }
    )
}