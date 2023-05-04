$(document).ready(function () {

    // Valid ID
    $('.modal-parent').on('click', 'i', function () {
        var img = $(this).attr('data-img')
        
        $('#imgModal').attr('src', img);
        $('#btnModal').click();
    });

    // Business Permit
    $('.modal-parent-1').on('click', 'i', function () {
        var img1 = $(this).attr('data-img-1')
                
        $('#imgModal1').attr('src', img1);
        $('#btnModal1').click();
    });

    // Add User
    $('.modal-add').on('click', function(e){
        e.preventDefault();
        $('#addUser').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Add Reseller
    $('.modal-add').on('click', function(e){
        e.preventDefault();
        $('#addReseller').modal('show').find('.modal-content').load($(this).attr('href'));
    });


    // Add Reseller
    $('.modal-add').on('click', function(e){
        e.preventDefault();
        $('#addReseller').modal('show').find('.modal-content').load($(this).attr('href'));
    });
    

    // Add Product
    $('.modal-add-prod').on('click', 'a', function(e){
        e.preventDefault();
        $('#addProductModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Add Product
    $('.modal-view-reason').on('click', 'a', function(e){
        e.preventDefault();
        $('#viewReasonModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Add Product
    $('.modal-add-res').on('click', 'a', function(e){
        e.preventDefault();
        $('#addResellerEmpty').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Add Product
    $('.modal-add-ret').on('click', 'a', function(e){
        e.preventDefault();
        $('#addReturnModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

        // // Add Reseller
        // $('.modal-add-res').on('click', function(e){
        //     e.preventDefault();
        //     $('#addResellerEmpty').modal('show').find('.modal-content').load($(this).attr('href'));
        // });
        

    // Select Product
    $('.modal-select-prod').on('click', 'a', function(e){
        e.preventDefault();
        $('#addToCart').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Register
    $('.modal-reg').on('click', 'a', function(e){
        e.preventDefault();
        $('#approveModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // View File
    $('.modal-view-file-VID').on('click', 'a', function(e){
        e.preventDefault();
        $('#viewFileModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    $('.modal-view-file-BP').on('click', 'a', function(e){
        e.preventDefault();
        $('#viewFileModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });
    
    // View Product
    $('.modal-view-product').on('click', 'a', function(e){
        e.preventDefault();
        $('#viewProductModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });
    
     // View Product
    $('.modal-view-stock').on('click', 'a', function(e){
        e.preventDefault();
        $('#haha').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // View Order
    $('.modal-view-order').on('click', 'a', function(e){
        e.preventDefault();
        $('#viewOrderModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Edit User
    $('.modal-edit').on('click', function(e){
        e.preventDefault();
        $('#editUser').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Edit User
    $('.modal-edit').on('click', function(e){
        e.preventDefault();
        $('#editProduct').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Edit User
    $('.modal-edit').on('click', function(e){
        e.preventDefault();
        $('#editReturn').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    // Receipt
    $('.modal-receipt').on('click', function(e){
        e.preventDefault();
        $('#receiptCart').modal('show').find('.modal-content').load($(this).attr('href'));
    });


    // Settings - Product
    $('.modal-add-fla').on('click', 'a', function(e){
        e.preventDefault();
        $('#addFlavorModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    $('.modal-add-cat').on('click', 'a', function(e){
        e.preventDefault();
        $('#addCategoryModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    $('.modal-add-unit').on('click', 'a', function(e){
        e.preventDefault();
        $('#addUnitModal').modal('show').find('.modal-content').load($(this).attr('href'));
    });

    $('.modal-add-prod-empty').on('click', 'a', function(e){
        e.preventDefault();
        $('#addProductEmpty').modal('show').find('.modal-content').load($(this).attr('href'));
    });
});

setTimeout(function() {
    $('.alert').fadeOut('slow');
}, 2000); // <-- time in milliseconds, 1000 =  1 sec



