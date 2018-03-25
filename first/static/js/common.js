$(document).ready(function () {

    /* Buttons */

    /*---------- event map ----------*/

    // $(".button_eventmap_more").click(function () {
    //     if($(this).hover()){
    //         $(".i_more").each(function () {
    //             $(this).toggleClass('i_active')
    //         })
    //     }
    // });

    /*---------- event map end ----------*/

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

    $(".iam_female").click(function () {
        // $(".block_mrs_ms").show();
        if ($(".lect_check_female").prop('checked')) {
            $(".block_mrs_ms").show();
        }
    });

    $(".iam_lect").click(function () {
        $(".block_sexus").show();
    });

    $(".iam_organ").click(function () {
        $(".block_sexus").hide();
    });

    if ($('#check_organ').prop('checked')) {
        $(".block_sexus").hide();
    }

    /*---------- reg ----------*/

    $(".iam_male").click(function () {
        $(".block_mrs_ms").hide();
    });

    /*--------------------*/

    $(".butt_close_erorrs").click(function () {
        $(".block_erorr_sign_in").hide();
        $(".block_erorr_register").hide();
    });

    $(".button_congrat").click(function () {
        $(".block_congratulation").hide();
    });

    $(".button_close_activprof").click(function () {
        $(".block_activate_profile").hide();
    });

    $(this).keydown(function (eventObject) {
        if (eventObject.which == 27) {
            $(".block_erorr_sign_in").hide();
            $(".block_erorr_register").hide();
            $(".block_congratulation").hide();
            $(".block_activate_profile").hide();
        }
    });

    /*---------- lectures ----------*/

    $(".lectures_plan").click(function () {
        $(this).addClass('lectures_active');
        $(".lectures_comp").removeClass('lectures_active');
        $(".lectures_canc").removeClass('lectures_active');
        $(".planned_lectures").show();
        $(".complended_lectures").hide();
        $(".canceled_lectures").hide();
    });

    $(".lectures_comp").click(function () {
        $(".lectures_plan").removeClass('lectures_active');
        $(this).addClass('lectures_active');
        $(".lectures_canc").removeClass('lectures_active');
        $(".planned_lectures").hide();
        $(".complended_lectures").show();
        $(".canceled_lectures").hide();
    });

    $(".lectures_canc").click(function () {
        $(".lectures_plan").removeClass('lectures_active');
        $(".lectures_comp").removeClass('lectures_active');
        $(this).addClass('lectures_active');
        $(".planned_lectures").hide();
        $(".complended_lectures").hide();
        $(".canceled_lectures").show();
    });

    /*---------- lectures end ----------*/

    /*---------- platforms ----------*/

    $(".platf_li_yo").click(function () {
        $(".platf_li_cr").removeClass('platf_active');
        $(this).addClass('platf_active');
        $('.platf_your_platf').show();
        $('.platf_create').hide();
        $('.platf_map_layer').hide();
        $(".platf_text_map_layer").hide()
    });

    $(".platf_li_cr").click(function () {
        $(".platf_li_yo").removeClass('platf_active');
        $(this).addClass('platf_active');
        $('.platf_create').show();
        $('.platf_your_platf').hide();
        $('.platf_map_layer').show();
    });

    $(".platf_map_layer").click(function () {
        $(".platf_text_map_layer").show()
    });

    /*---------- platforms end ----------*/
    $(".app_lect_li_your").click(function () {
        $(this).addClass('app_li_active');
        $(".app_lect_li_con").removeClass('app_li_active');
        $('.app_lect_your_apps').show();
        $('.app_lect_considered_apps').hide();
    });

    $(".app_lect_li_con").click(function () {
        $(".app_lect_li_your").removeClass('app_li_active');
        $(this).addClass('app_li_active');
        $('.app_lect_your_apps').hide();
        $('.app_lect_considered_apps').show();
    });


    $(".app_organ_li_sub").click(function () {
        $(this).addClass('app_li_active');
        $(".app_organ_li_con").removeClass('app_li_active');
        $(".app_organ_li_com").removeClass('app_li_active');
        $(".app_organ_li_rej").removeClass('app_li_active');
        $('.app_organ_submitted_apps').show();
        $('.app_organ_confirmed_apps').hide();
        $('.app_organ_completed_apps').hide();
        $('.app_organ_rejected_apps').hide();
    });

    $(".app_organ_li_con").click(function () {
        $(".app_organ_li_sub").removeClass('app_li_active');
        $(this).addClass('app_li_active');
        $(".app_organ_li_com").removeClass('app_li_active');
        $(".app_organ_li_rej").removeClass('app_li_active');
        $('.app_organ_submitted_apps').hide();
        $('.app_organ_confirmed_apps').show();
        $('.app_organ_completed_apps').hide();
        $('.app_organ_rejected_apps').hide();
    });

    $(".app_organ_li_com").click(function () {
        $(".app_organ_li_sub").removeClass('app_li_active');
        $(".app_organ_li_con").removeClass('app_lin_active');
        $(this).addClass('app_li_active');
        $(".app_organ_li_rej").removeClass('app_li_active');
        $('.app_organ_submitted_apps').hide();
        $('.app_organ_confirmed_apps').hide();
        $('.app_organ_completed_apps').show();
        $('.app_organ_rejected_apps').hide();
    });

    $(".app_organ_li_rej").click(function () {
        $(".app_organ_li_sub").removeClass('app_li_active');
        $(".app_organ_li_con").removeClass('app_li_active');
        $(".app_organ_li_com").removeClass('app_li_active');
        $(this).addClass('app_li_active');
        $('.app_organ_submitted_apps').hide();
        $('.app_organ_confirmed_apps').hide();
        $('.app_organ_completed_apps').hide();
        $('.app_organ_rejected_apps').show();
    });

    /*---------- applications ----------*/

    /*---------- applications end ----------*/

    /* ---> Buttons end <--- */


    function submit_form() {

        $('.avatar_form').submit()

    }

});

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