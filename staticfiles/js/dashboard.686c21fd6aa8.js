// $(document).ready(function () {
//     var fieldValue = $('#id_your_field').text().trim();
//     if (fieldValue === '') {
//         $('#id_your_field').text('Php 0.00');
//     }    
// });

$(document).ready(function () {
    $("#searchInput").on("keyup", function() {
        var searchValue = $(this).val().toLowerCase();
        $("#sidebar li").each(function() {
            var listItem = $(this);
            if (searchValue === '') {
                listItem.show();
                listItem.find(".nav-link").addClass("collapsed");
                listItem.find(".nav-content").removeClass("show");
            } else if (listItem.text().toLowerCase().indexOf(searchValue) !== -1 || listItem.find('*').filter(function() {
                return $(this).text().toLowerCase().indexOf(searchValue) !== -1;
            }).length) {
                listItem.show();
                listItem.find(".nav-link").removeClass("collapsed");
                listItem.find(".nav-content").addClass("show");
            } else {
                listItem.hide();
            }
        });
    });
});