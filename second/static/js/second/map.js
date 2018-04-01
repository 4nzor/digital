function initMapSearch() {

    var centr_search = {lat: 43.457, lng: 34.311};

    var map_search = new google.maps.Map(document.getElementById('search_map'), {
        zoom: 6,
        maxZoom: 10,
        center: centr_search
    });

}

google.maps.event.addDomListener(window, 'load', initMapSearch);