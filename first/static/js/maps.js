function initMap(url) {
    jQuery.ajax({
       type:'GET',
        url:'/api/v1/eventmap/',

       success :function (data) {
           let uluru = {lat: 43.457, lng: 34.311};

           let map = new google.maps.Map(document.getElementById('map'), {
               zoom: 3,
               center: uluru
           });
           for (i = 0; i < data.event_coords.length; i++) {

               let lat = parseFloat(data.event_coords[i].lat);
               let lng = parseFloat(data.event_coords[i].lng);


               let LatLng = {lat: lat, lng: lng};
               let marker = new google.maps.Marker({
                   animation: google.maps.Animation.DROP,
                   position: LatLng,
                   map: map,
                   icon: url
               });
               markers.push(marker)


           }
       }

    });


}
google.maps.event.addDomListener(window, 'load', initMap('https://habrastorage.org/webt/ki/ru/nw/kirunwnagzq2tnrgxcaqaktv9ia.png'));
/*
function initMap2() {

    var uluru2 = {lat: 43.457, lng: 34.311};

    var map2 = new google.maps.Map(document.getElementById('map2'), {
        zoom: 6,
        center: uluru2
    });

    google.maps.event.addListener(map2, 'click', function (event) {
        addMarker(event.latLng, map2);
    });

    addMarker(uluru2, map2);

    function addMarker(location, map2) {

        let markerImage = 'https://psv4.userapi.com/c834502/u187881541' +
            '/docs/d5/7cdea22a5d38/lect.png?extra=3ik8bvlrIhS' +
            'UjQe0kw8JkVTdyTrVsBdOtgHqtdRjkPb4WlNqcd7OLfQRJcuK2pUh' +
            'XjxY7Rjx65NhtX4EJDfd389sEG3ZhpnrJoNZ8LKT7a-6_nfBKlFm_lF' +
            'VXQ3bAYJFMHtNFfirA0OC5tRD'

        let marker = new google.maps.Marker({
            animation: google.maps.Animation.DROP,
            position: location,
            map: map2,
            icon: markerImage
        });

        popupContent = '<p class="content">Что угодно</p>';

        infowindow = new google.maps.InfoWindow({
            content: popupContent
        });

        infowindow.open(map2, marker);

        marker.addListener('click', function () {
            infowindow.open(map2, marker);
        });
    }

}


 google.maps.event.addDomListener(window, 'load', initMap2);*
 "Старый код для lectures"*/


//Приветсвтвую тебя ,странник

function async_check_coords() {
    jQuery.ajax({
        type: 'GET',
        url: '/api/v1/check_coors/',

        success: function (data) {
            let lat_lng = {
                lat: 47.220983, lng: 38.917300
            };
            map = new google.maps.Map(document.getElementById('map_platf'), {

                zoom: 7,
                center: lat_lng,
                mapTypeId: google.maps.MapTypeId.TERRAIN
            });

            for (i = 0; i < data.data.length; i++) {
                let marker = new google.maps.Marker({
                    animation: google.maps.Animation.DROP,
                    position: data.data[i],
                    map: map,
                    label: data.name[i].name,
                    icon:'https://habrastorage.org/webt/ki/ru/nw/kirunwnagzq2tnrgxcaqaktv9ia.png',

                });


            }
        }
    })
}

function initMapPlatf() {
    var lat_lng = {lat: 17.08672, lng: 78.42444};
    map = new google.maps.Map(document.getElementById('map_platf'), {
        zoom: 7,
        center: lat_lng,
        mapTypeId: google.maps.MapTypeId.TERRAIN
    });

    // This event listener will call addMarker() when the map is clicked.
    map.addListener('click', function (event) {
        addMarker(event.latLng);
    });


}

markers = [];

function addMarker(location) {
    function setMapOnAll(map) {
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(map);
        }
    }

    function clearMarkers() {
        setMapOnAll(null);
    }

    clearMarkers();
    markers = [];
    var marker = new google.maps.Marker({

        animation: google.maps.Animation.DROP,
        position: location,
        map: map,
        icon:'https://habrastorage.org/webt/ki/ru/nw/kirunwnagzq2tnrgxcaqaktv9ia.png',


    });

    markers.push(marker);

    document.getElementById('input_lat').value = marker.position.lat();
    document.getElementById('input_lng').value = marker.position.lng();
    infowindow.open(map, marker);
}

google.maps.event.addDomListener(window, 'load', initMapPlatf);