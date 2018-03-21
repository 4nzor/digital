$(document).ready(function () {

    /* Buttons */

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
    });

    $(".butt_close_erorrs").click(function () {
        $(".block_erorr_sign_in").hide();
        $(".block_erorr_register").hide();
    });

    $(".button_congrat").click(function () {
        $(".block_congratulation").hide();
    });

    $(this).keydown(function (eventObject) {
        if (eventObject.which == 27) {
            $(".block_erorr_sign_in").hide();
            $(".block_erorr_register").hide();
            $(".block_congratulation").hide();
        }
    });

    /* ---> Buttons end <--- */

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

                if (data.msg === 'None') {
                    $('.bg_photo_lect').remove();
                    $('.avatar_image2').attr("src", data.url)
                    $('.avatar_image2').css('display', 'block');

                }
                else {

                    $('.avatar_image2').css('display', 'none');
                    $('.avatar_image').attr("src", data.url)
                }


            }


        });
    }
});