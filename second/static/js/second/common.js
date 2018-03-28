$(document).ready(function () {

    $(".menu_button_show").click(function () {
       $(this).hide();
       $('.main_menu').addClass('menu_active');
    });

    $(".menu_button_hide").click(function () {
       $(".menu_button_show").show();
       $('.main_menu').removeClass('menu_active');
    });

});
