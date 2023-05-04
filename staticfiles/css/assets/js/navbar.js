$(document).ready(function() {
    $("#closeNav").click(function() {
        $("#menuNav").removeClass("show");
        $("#navbar").removeClass("no-scroll");
    });
    
    if ($(window).scrollTop() >= 50) {
        $('#toTop').fadeIn(200);
    } 
    else {
        $('#toTop').fadeOut(200);
    }
    
    $(window).scroll(function() {
        if ($(this).scrollTop() >= 50) {
            $('#toTop').fadeIn(200);
        } 
        else {
            $('#toTop').fadeOut(200);
        }
    });
    
    $('#toTop').click(function() {
        $('body,html').animate({
            scrollTop: 0
        }, 500);
    });

    // $('[toggle="tooltip"]').tooltip();   

    $('.category').mouseenter(function() {
        $(this).find('.tooltip').fadeIn();
    }).mouseleave(function() {
    $(this).find('.tooltip').fadeOut();
    });
});
