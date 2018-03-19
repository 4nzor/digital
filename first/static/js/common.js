function initMap() {

    var uluru = {lat: 43.457, lng: 34.311};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: uluru
    });

}

$(".settings_lecturer").click(function () {
    $(".lect_sex").toggle();
    $(".lect_parag input").toggle();
    $(".lect_parag select").toggle();
    $(".info_lect").toggle();
    $(".lect_subm").toggle();
    $(".lecturer_name").toggle();
});

$(".lect_subm").click(function () {
    $(".lect_sex").hide();
    $(".lect_parag input").hide();
    $(".lect_parag select").hide();
    document.location.reload()
});

$(".settings_organizer").click(function () {
    $(".organ_parag input").toggle();
    $(".organ_parag select").toggle();
    $(".info_organ").toggle();
    $(".organ_subm").toggle();
    $(".organizer_name").toggle();
});

$(".organ_subm").click(function () {
    $(".organ_parag input").hide();
    $(".organ_parag select").hide();
    document.location.reload()
});

$(".lect_check_female").click(function () {
    $(".block_mrs_ms").show();
    if ($(this).prop('checked')) {
        $(".block_mrs_ms").show();
    }
});

$(".lect_check_male").click(function () {
    $(".block_mrs_ms").hide();
    // if ($(this).prop('checked')) {
    //     $(".block_mrs_ms").hide();
    // }
});

function submit_form() {

    $('.avatar_form').submit()

}

function ajax_avatar() {

    var avatar_form = $('.avatar_form');

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

        success: function (data) {

            console.log(data);
            $('.avatar_image').attr("src", data.url);
        }
    });
}