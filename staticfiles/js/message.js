$(document).ready(function submitForm(form) {
    var message = "Do you really want to <b>archive</b> this reseller?";
    
    swal({
        title: "Archive",
        // text: "Do you really want to <span>archive</span> this reseller?",
        content: {
            element: 'p',
            attributes: {
                innerHTML: message,
            }
        },
        
        // icon: "warning",
        buttons: {
            // confirm: "Yes",
            confirm: {
                text: "Yes",
            },
            cancel: true,
        },
        className: 'swal-wide',
        dangerMode: true,
        // allowOutsideClick: false,
        closeOnClickOutside: false

        
        
    })
    .then(function (isConfirm) {
        if (isConfirm) {
            form.submit();
        }
    });
    return false;
});

