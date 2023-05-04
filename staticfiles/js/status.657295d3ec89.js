$(document).ready(function () {
    // badge-status
    
    $('.badge-status').filter(function () {
        return $(this).text() == 'inactive';
    }).removeClass('bg-primary')
        .addClass('bg-danger')

    $('.badge-status').filter(function () {
        return $(this).text() == 'active';
    }).removeClass('bg-danger')
        .addClass('bg-primary')

    $('.badge-status').filter(function () {
        return $(this).text() == 'pending';
    }).removeClass('bg-danger')
        .addClass('bg-pending')


    $('.badge-status').filter(function () {
        return $(this).text() == 'unreturned';
    }).removeClass('bg-danger')
        .addClass('bg-pending')

    $('.badge-status').filter(function () {
        return $(this).text() == 'returned';
    }).removeClass('bg-danger')
        .addClass('bg-primary')


    // badge-status

    $('.badge-stat-res').filter(function () {
        return $(this).text() == 'Pending';
    }).removeClass('bg-primary')
        .removeClass('bg-out')
        .addClass('bg-pending')

    $('.badge-stat-res').filter(function () {
        return $(this).text() == 'Out for Shipping';
    }).removeClass('bg-primary')
        .addClass('bg-out')
        .removeClass('bg-pending')

    $('.badge-stat-res').filter(function () {
        return $(this).text() == 'Out for Delivery';
    }).removeClass('bg-primary')
        .addClass('bg-out')
        .removeClass('bg-pending')

    $('.badge-stat-res').filter(function () {
        return $(this).text() == 'In Process';
    }).removeClass('bg-primary')
        .addClass('bg-process')
        .removeClass('bg-pending')

    $('.badge-stat-res').filter(function () {
        return $(this).text() == 'Completed';
    }).addClass('bg-primary')
        .removeClass('bg-out')
        .removeClass('bg-pending')


    


});

