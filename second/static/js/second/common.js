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
    });

    $(".menu_button_hide").click(function () {
        $(".menu_button_show").show();
        $('.menu_content').removeClass('menu_active');
        $('.main_menu').removeClass('menu_active');
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
            $(".search_block_submit").addClass('search_submit_active');
            $(".search_content").addClass('search_content_active')
        }
        else {
            $(".search_adv_block").removeClass('search_adv_active');
            $(".search_block_submit").removeClass('search_submit_active');
            $(".search_content").removeClass('search_content_active')
        }
    });

});
