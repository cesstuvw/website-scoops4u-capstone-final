$(document).ready(function () {
     // Hide pending order
    if (!$("#desc-profile").text()){
        $(".empty-screen2").removeClass("d-none");
        
    }
    else{
        $(".empty-screen2").addClass("d-none");
    };
});

