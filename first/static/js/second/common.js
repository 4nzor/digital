$(document).ready(function () {

    if ($(".search_checked_map input").is(':checked')) {
        $(".search_block").addClass('search_block_active');
        $(".search_map_block").addClass('map_block_active');
        $(".search_mob_open").addClass('search_mob_open_active');
    }
    else {
        $(".search_block").removeClass('search_block_active');
        $(".search_map_block").removeClass('map_block_active');
        $(".search_mob_open").removeClass('search_mob_open_active');
    }

    if ($(".search_checked_advsearch input").is(':checked')) {
        $(".search_adv_block").addClass('search_adv_active');
        $(".search_bg_sum").addClass('search_submit_active');
        $(".search_content").addClass('search_content_active');
        $(".search_adv_block input").css("display", "block");
    }
    else {
        $(".search_adv_block").removeClass('search_adv_active');
        $(".search_bg_sum").removeClass('search_submit_active');
        $(".search_content").removeClass('search_content_active')
    }

    $(".menu_button_show").click(function () {
        $(this).addClass('butt_active');
        $('.menu_content').addClass('menu_active');
        $('.main_menu').addClass('menu_active');
        $('.search_block').fadeOut(250);
        $('.home_block').fadeOut(250);
        $('.quest_block').fadeOut(250);
        $('.about_block').fadeOut(250);
        $('.profile_block').fadeOut(250);
        $('.signin_block').fadeOut(250);
        $('.rslts_block').fadeOut(250);
    });

    $(".menu_button_hide").click(function () {
        $('.menu_button_show').removeClass('butt_active');
        $('.menu_content').removeClass('menu_active');
        $('.main_menu').removeClass('menu_active');
        $('.search_block').show();
        $('.home_block').show();
        $('.quest_block').show();
        $('.about_block').show();
        $('.profile_block').show();
        $('.signin_block').show();
        $('.rslts_block').show();
    });

    $(".search_checked_map").click(function () {
        if ($(".search_checked_map input").is(':checked')) {
            $(".search_block").addClass('search_block_active');
            $(".search_map_block").addClass('map_block_active');
            $(".search_mob_open").addClass('search_mob_open_active');
        }
        else {
            $(".search_block").removeClass('search_block_active');
            $(".search_map_block").removeClass('map_block_active');
            $(".search_mob_open").removeClass('search_mob_open_active');
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

    $(".search_mob_open").click(function () {
        $(".search_block").addClass('search_block_active');
        $(".search_map_block").addClass('map_block_active');
    });

    $(".search_mob_close").click(function () {
        $(".search_block").removeClass('search_block_active');
        $(".search_map_block").removeClass('map_block_active');
    })


    /* create input */

    // var cr_input = document.createElement('input');

    // $(".quest_create_quest").click(function () {
    //     $(".quest_block_inputs form").append('<input type="text">');
    // });

    //* results *//

    var lihe = document.getElementById('lihe');

    lihe.onmousedown = function (e) {

        lihe.style.position = 'absolute';

        moveAt(e);

        document.body.appendChild(lihe);

        lihe.style.zIndex = 10000;
        lihe.style.left = 50 + "%";
        lihe.style.marginLeft = -475 + "px";
        lihe.style.cursor = "pointer";


        function moveAt(e) {

            lihe.style.top = e.pageY - lihe.offsetHeight / 2 + 'px';
        }

        document.onmousemove = function (e) {
            moveAt(e);
        };

        lihe.onmouseup = function () {
            document.onmousemove = null;
            lihe.onmouseup = null;
        }
    };

    lihe.ondragstart = function () {
        return false;
    };

});


