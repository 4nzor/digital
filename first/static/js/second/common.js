$(document).ready(function () {

    if ($(".search_checked_map input").is(':checked')) {
        $(".search_block").addClass('search_block_active');
        $(".search_map_block").addClass('map_block_active')
    }
    else {
        $(".search_block").removeClass('search_block_active');
        $(".search_map_block").removeClass('map_block_active')
    }

    if ($(".search_checked_advsearch input").is(':checked')) {
        $(".search_adv_block").addClass('search_adv_active');
        $(".search_block_submit").addClass('search_submit_active');
        $(".search_content").addClass('search_content_active')
    }
    else {
        $(".search_adv_block").removeClass('search_adv_active');
        $(".search_block_submit").removeClass('search_submit_active');
        $(".search_content").removeClass('search_content_active')
    }

    $(".menu_button_show").click(function () {
        $(this).hide();
        $('.menu_content').addClass('menu_active');
        $('.main_menu').addClass('menu_active');
        $('.search_block').hide();
        $('.quest_block').hide();
        $('.about_block').hide();
    });

    $(".menu_button_hide").click(function () {
        $(".menu_button_show").show();
        $('.menu_content').removeClass('menu_active');
        $('.main_menu').removeClass('menu_active');
        $('.search_block').show();
        $('.quest_block').show();
        $('.about_block').show();
    });

    $(".search_checked_map").click(function () {
        if ($(".search_checked_map input").is(':checked')) {
            $(".search_block").addClass('search_block_active');
            $(".search_map_block").addClass('map_block_active')
        }
        else {
            $(".search_block").removeClass('search_block_active');
            $(".search_map_block").removeClass('map_block_active')
        }
    });

    $(".search_checked_advsearch").click(function () {
        if ($(".search_checked_advsearch input").is(':checked')) {
            $(".search_adv_block").addClass('search_adv_active');
            $(".search_bg_sum").addClass('search_submit_active');
            $(".search_content").addClass('search_content_active');
            $(".search_adv_block input").show();
        }
        else {
            $(".search_adv_block").removeClass('search_adv_active');
            $(".search_bg_sum").removeClass('search_submit_active');
            $(".search_content").removeClass('search_content_active');
            $(".search_adv_block input").hide(700);
        }
    });

    /* create input */

    // var cr_input = document.createElement('input');

    $(".quest_create_quest").click(function () {
        $(".quest_block_inputs form").append('<input type="text">');
    })

});
