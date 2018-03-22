function initMap() {

    var uluru = {lat: 43.457, lng: 34.311};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: uluru
    });

}

google.maps.event.addDomListener(window, 'load', initMap);

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

        // var markerImage = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';

        var marker = new google.maps.Marker({
            animation: google.maps.Animation.DROP,
            position: location,
            map: map2,
            // icon: markerImage
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

google.maps.event.addDomListener(window, 'load', initMap2);