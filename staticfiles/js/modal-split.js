$(document).ready(function() {
    
    prep_modal();

    $('input[type="checkbox"]').on('change', function(e){
        if(e.target.checked){
            $('#staticBackdrop').modal('show');
            $('.btn-send').fadeToggle(1000).removeClass('d-none');
        }
        else{
            $('.btn-send').fadeToggle(800);
        }
    });

    // $('.btn-container').on('click', function(e){
    //     e.preventDefault();
    //     $('#archiveUser').modal('show');
    // });

    // $('.modal-edit').on('click', function(e){
    //     e.preventDefault();
    //     $('#archiveUser').modal('show').find('.modal-content').load($(this).attr('href'));
    // });
});

    function prep_modal()
    {
        $(".modal").each(function() {
    
        var element = this;
        var pages = $(this).find('.modal-split');
    
        if (pages.length != 0)
        {
            pages.hide();
            pages.eq(0).show();
    
            var b_button = document.createElement("button");
                    b_button.setAttribute("type","button");
                            b_button.setAttribute("class","btn btn-primary");
                            b_button.setAttribute("style","display: none;");
                            b_button.innerHTML = "Back";

            var n_button = document.createElement("button");
                    n_button.setAttribute("type","button");
                            n_button.setAttribute("class","btn btn-primary");
                            n_button.innerHTML = "<i class='ri-arrow-right-s-line'></i>";
    
            $(this).find('.modal-footer').append(b_button).append(n_button);
    
    
            var page_track = 0;
    
            $(n_button).click(function() {
            
            this.blur();
    
                if(page_track == 0) 
                {
                    $(b_button).show();
                }
    
                if(page_track == pages.length-2)
                {
                    $(b_button).html("<i class='ri-arrow-left-s-line'></i>").show();
                    $(n_button).html("<span data-bs-dismiss='modal'>Close</span>");
                }
    
            if(page_track == pages.length-1)
            {
                $(element).find("form").submit();
            }
    
                if(page_track < pages.length-1)
                {
                    page_track++;
    
                    pages.hide();
                    pages.eq(page_track).show();
                }
    
    
            });
    
            $(b_button).click(function() {
    
                if(page_track == 1)
                {
                    $(b_button).hide();
                }
    
                if(page_track == pages.length-1)
                {
                    $(b_button).html("Back").show();
                    $(n_button).html("<i class='ri-arrow-right-s-line'></i>");
                }
    
                if(page_track > 0)
                {
                    page_track--;
    
                    pages.hide();
                    pages.eq(page_track).show();
                }
    
    
            });
    
        }
    
        });
    }

    
