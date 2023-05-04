$(document).ready(function(){
    var qty = parseInt($('#qty').val())
    var qtys = parseInt(qty)
    $('#btn_checkout').click(function(e) {
        if( qtys == 0){
            e.preventDefault();
        } 
    });
    
})