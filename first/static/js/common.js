function initMap() {

    var uluru = {lat: 43.457, lng: 34.311};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: uluru
    });

}

$(".settings_lecturer").click(function () {
    $(".lect_sex").show();
    $(".lect_parag input").show();
    $(".lect_parag select").show();
    $(".info_lect").hide();
    $(".lect_subm").show();
});

$(".lect_subm").click(function () {
    $(".lect_sex").hide();
    $(".lect_parag input").hide();
    $(".lect_parag select").hide();
    document.location.reload()
});



function submit_form() {

    $('.avatar_form').submit()

}
function ajax_avatar()
{

    var avatar_form   = $('.avatar_form');

    var form = new FormData(avatar_form.closest('form').get(0));
    jQuery.ajax({
        type: 'POST',
        url: '/upload_avatar/',
        async: true,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        data: form,

        success: function(data) {

            console.log(data);
            $('.avatar_image').attr("src", data.url);
        }
    });
}