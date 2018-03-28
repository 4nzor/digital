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



//Приветсвтвую тебя ,странник

function async_check_coords() {
    jQuery.ajax({
        type: 'GET',
        url: '/api/v1/check_coors/',

    success:function (data) {
        var lat_lng = {lat: 47.220983, lng: 38.917300
        };
        map = new google.maps.Map(document.getElementById('map_platf'), {

            zoom: 7,
            center: lat_lng,
            mapTypeId: google.maps.MapTypeId.TERRAIN
        });

        for(i=0 ;i<data.data.length;i++) {
            console.log(data.data[i].lat);
            console.log(data.data[i].lon);
            var marker = new google.maps.Marker({
                animation: google.maps.Animation.DROP,
                position:data.data[i],
                map: map,
                label:data.name[i].name
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
markers=[];
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

    });

    markers.push(marker);

    document.getElementById('input_lat').value = marker.position.lat();
    document.getElementById('input_lng').value = marker.position.lng();
    infowindow.open(map, marker);
}

google.maps.event.addDomListener(window, 'load', initMapPlatf);