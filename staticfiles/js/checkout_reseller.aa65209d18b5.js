$(document).ready(function(){
    var total_amount = parseInt($('#amount').val())
    var discount = parseInt($('#discount').val())

    var result =   total_amount - discount
    var currency = parseFloat(result).toLocaleString('en-PH', { style: 'currency', currency: 'PHP', currencyDisplay: 'code' }).replace('PHP', 'Php');	

    $('#vgtotal').val(currency)	
    $('#gtotal').val(result)	
    $('#stotal').val(result)   



 
    $('#option').on('change', function () {
        var select_value = this.value
        if (select_value == "delivery") {
          
    
            // $('#pdate').css("display", "block")
        
            $('#pdate').fadeOut(1000)
            $('#no_specific').fadeOut(1000)
           
        } else if (select_value == "pickup") {
        
            $('#h3_date').text('Pickup Date')
            $('#pdate').fadeIn(1000)
          
            // $('#pdate').css("display", "none")
        } else if (select_value == "") {
            $('#pdate').fadeOut(1000)
            // $('#pdate').css("display", "none")
        }

    })

    $('#input_date').on('click', function () {
        $('#no_specific').fadeToggle(1000)
    })

    $('#checkbox_no_date').on('click', function () {
        $('#date_deliver').fadeToggle(1000)
        $('#input_date').val('')
    })



})