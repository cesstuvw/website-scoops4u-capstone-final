$(document).ready(function () {

    $('#password').keyup(function() {
        // If value is not empty
        if ($(this).val().length == 0) {
          // Hide the element
            $('#eye').hide();
        } else {
          // Otherwise show it
            $('#eye').show();
        }
      }).keyup(); // Trigger the keyup event, thus running the handler on page load

    $('#eye').click(function(){
    
    if($(this).hasClass("ri-eye-fill")){
        
        $(this).removeClass("ri-eye-fill");
        
        $(this).addClass("ri-eye-off-fill");
        
        $('#password').attr('type','text');
        
    }else{
        
        $(this).removeClass("ri-eye-off-fill");
        
        $(this).addClass("ri-eye-fill");  
        
        $('#password').attr('type','password');
    }
    });
});