
$(document).ready(function(){
    // var form = $('#form')
    // form.on('submit', function (e) {
    //     e.preventDefault();

       
    // })













    $('#btn_compute').on('click', function (e) {
        e.preventDefault();
        var total_amount = parseInt($('#total_amount').val())
        var cash = parseInt($('#cash').val())

        var result =  cash - total_amount
;
        // var formattedNumber = new result.toLocaleString('en-PH', options);
        var currency = parseFloat(result).toLocaleString('en-PH', { style: 'currency', currency: 'PHP', currencyDisplay: 'code' }).replace('PHP', 'Php');
       
        var msg = $('#msg')
        var pos_id = $('#pos_id').val()


        if(cash >= total_amount){
            $('#get_id').val(pos_id)
            $('#vchange').val(currency)
            $('#change').val(result).css('text-transform', 'capitalize');
            // $('#change').val(result.toLocaleString('en-PH', { style: 'currency', currency: 'PHP' }));

            // $('#btn-receipt').removeAttr('hidden');
            $('#btn-receipt').removeClass('d-none')	
            
            // $('#form').submit()


        }else{
            $('#msg').css("color", "red")
            // $('#msg').css("fontSize", "20px")
            $('#msg').css("display", "block")
            msg.html('<i class="msg">Insufficient Payment<i/>')
            // msg.html('<p class="msg">Insufficient Payment</p>')
            $('#vchange').val("Php 0.00").css('text-transform', 'capitalize');
            setTimeout(function() {
                $('#msg').css("display", "none");
            }, 3000);
        }
        
    })

    $('#btn-receipt').on('click', function(e){
        e.preventDefault()
        var cash = $('#cash').val()
        // var change = $('#change').val()
        
        if(cash == "" ){
            alert('all field required')
        }else if(cash.length > 12){
            alert('invalid cash')
        }else{
            $('#form').submit()
        }


    })

    $('#return').change(function() {	
        var defaultCash = 0	
        var sumAmount= $('#sum_amount').val()
        if(this.checked) {	
            $('#total_amount').val(0)
            $('.cash').addClass('d-none')
            $('.change').addClass('d-none')
            $('#cash').val(defaultCash)
            $('#vchange').val("Php 0.00")	
            $('#change').val(0)	
            $('#btn-receipt').removeClass('d-none')
            $('#btn_compute').addClass('d-none')
        
        } else {	
            $('#total_amount').val(sumAmount)	
            $('#btn-receipt').addClass('d-none')	
            $('.cash').removeClass('d-none')
            $('.change').removeClass('d-none')
            $('#btn_compute').removeClass('d-none')	
            $('#cash').val("")	
            $('#vchange').val("")	
    
        }	
        // if($(this).is(':checked')) {	
        //     $('#cash').val(defaultCash)	
        //     $('#btn-receipt').fadeIn(1000)	
    
        // } else {	
        //     $('#cash').val("")	
        //     $('#btn-receipt').fadeOut(1000)	
        // }	
    });


    if ($("#posTable > tbody > tr").length == null || $("#posTable > tbody > tr").length == 0){
        $("#removeAll").addClass("d-none");
        $("#orderSummary").addClass("d-none");

    }
    else{
        $("#removeAll").removeClass("d-none");
        $("#orderSummary").removeClass("d-none");
    };

    $('#btnCart').on('click', function(e){
        e.preventDefault();
        $('#addToCart').modal('show');
    });

})




