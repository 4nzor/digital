ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("mapsearch", {
        center: [55.76, 37.64],
        zoom: 7
    });


        var myGeocoder = ymaps.geocode("Roma");
    myGeocoder.then(
    function (res) {
        console.log(res.geoObjects.get(0).geometry.getCoordinates())
    },
    function (err) {
        // обработка ошибки
    }
);


    $.ajax({
        url: '/database/get_points',
        type: 'GET',

        success: function (data) {
            var coords = [];
            for (var i = 0; i < data.length; i++)
                coords.push([data[i].lat, data[i].lon])

            var myGeoObjects = [];

    for (var j = 0; j < coords.length; j++) {
        myGeoObjects[j] = new ymaps.GeoObject({
            geometry: {
                type: "Point",
                coordinates: coords[j]
            },
            properties: {
                clusterCaption: data[j].org_name,
                balloonContentBody: data[j].country
            }
        });
    }

    var myClusterer = new ymaps.Clusterer(
        {clusterDisableClickZoom: true}
    );
    myClusterer.add(myGeoObjects);
    myMap.geoObjects.add(myClusterer);

        }
    });

}
