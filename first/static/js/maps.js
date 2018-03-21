function initMap() {

        var uluru = {lat: 43.457, lng: 34.311};

        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 6,
            center: uluru
        });

    }