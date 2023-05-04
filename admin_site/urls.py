from django.urls import path
from admin_site import views
from django.conf.urls.static import static



app_name = 'admin_site'
urlpatterns = [
    path('', views.dashboard_admin, name='dashboard'),
    path('user-list/', views.user_list , name='user_list'),
    path('edit-user-list/<int:userid>/', views.edit_user_account, name='edit_user_account'),
    path('add-useraccount/', views.add_useraccount, name='add_useraccount'),
    path('update-user-list/<int:userid>/', views.update_user_account , name='update_user_account'),

    path('list-inquiry/', views.list_inquiry, name='list_inquiry'),
    path('list-reseller/', views.list_reseller, name='list_reseller'),
    path('edit-reseller/<int:id>/', views.edit_reseller, name='edit_reseller'),
    path('update-reseller/<int:id>/', views.update_reseller, name='update_reseller'),
    path('archive-reseller/<int:resellerid>/', views.archive_reseller, name='archive_reseller'),

    path('add_profile/', views.add_profile, name='add_profile'),
    path('update_profile/<int:profileid>', views.update_profile, name='update_profile'),

    path('My-profile/', views.my_profile, name='my_profile'),



    path('list-archive-reseller/', views.list_archive, name='list_archive'),
    path('retrieve-reseller/<int:id>/', views.retrieve_reseller, name='retrieve_reseller'),



    # path('send-email/', views.send_email, name='send_email'),
    path('send-email/<int:id>/', views.send_email, name='send_email'),
    path('send-email-reseller/<int:id>/', views.send_email_reseller, name='send_email_reseller'),    



    path('process/inquiry/', views.process_inquiry, name='process_inquiry'),

    #adding reseller 
    path('adding-reseller/', views.add_reseller, name='add_reseller'),

    path('product/', views.list_products, name='list_product'),
    path('view-product/<int:productid>/', views.view_product, name='view_product'),
    path('add-product/', views.add_product, name='add_product'),
    path('Process-product/', views.process_product, name='process_product'),
    path('edit-product/<int:productid>/', views.edit_product, name='edit_product'),
    path('update-product/<int:productid>/', views.update_product, name='update_product'),


    path('inventory/', views.inventory, name='inventory'),
    path('view-inventory/', views.view_inventory, name='view_inventory'),
   
    path('update-inventory/<int:productid>/', views.update_inventory, name='update_inventory'),

    path('pos/', views.pos ,name='pos'),
    path('pos-receipt/', views.pos_receipt ,name='pos_receipt'),
    path('pos-remove/', views.pos_removeall ,name='pos_removeall'),
    path('pos-receipt/', views.Click_receipt ,name='click_receipt'),
    
    path('pos/add-receipt/', views.pos_addreceipt ,name='add_receipt'),
    path('pos/receipt-process/', views.pos_receipt_process ,name='receipt_process'),

    path('minus-qty/<int:productid>/', views.minus_qty, name='minus_qty'),
    path('add-qty/<int:productid>/', views.add_qty ,name='add_qty'),

    path('pos/cancel/<int:productid>/', views.pos_cancel,name='pos_cancel'),


    path('pos/all-products/', views.all_products ,name='all_products'),
    path('cart/all-products/<int:productid>/', views.cart_products ,name='cart_products'),

    path('transaction-orders/pending', views.Transaction_orders, name='transaction_orders'),

# new status
    path('transaction-orders/in-process', views.in_process, name='in_process'),
    path('transaction-orders/in process', views.Transaction_in_process, name='transaction_in_process'),

    path('transaction-orders/process-out-for-delivery', views.delivery_process, name='delivery_process'),
    path('transaction-orders/out for shipping', views.Transaction_outshipping, name='transaction_outshipping'),

    path('transaction-orders/completed', views.Transaction_completed, name='transaction_completed'),
    path('transaction-orders/process-completed', views.completed_process, name='completed_process'),

    path('transaction-view/<int:id>/', views.transaction_view, name='transaction_view'),
    
    #search 
    path('search-reseller/', views.search_reseller, name='search_reseller'),
    path('search-archive-reseller/', views.search_archive, name='search_archive_reseller'),
    path('search-product/', views.search_product, name='search_product'),
    path('search-inventory/', views.search_inventory, name='search_inventory'),
    path('search-transaction/', views.search_transaction, name='search_transaction'),
    path('search/activity-log/', views.search_actlog, name='search_act-log'),
    path('search/activity-log-date/', views.search_date_actlog, name='search_date_actlog'),
    path('search/online-sales', views.search_online_sales, name='search_online_sales'),
    path('search/pos-sales', views.search_pos_sales, name='search_pos_sales'),

    #report
    path('reports/activity-log/', views.report_actlog, name='report_actlog'),
    path('reports/pos-sales/', views.report_pos_sales, name='report_pos_sales'),
    path('reports/online-sales/', views.report_online_sales, name='report_online_sales'),
    path('reports/users/', views.report_users, name='report_users'),
    path('reports/resellers/', views.report_res, name='report_res'),
    path('reports/product/', views.report_product, name='report_product'),
    path('reports/stocks/', views.report_stocks, name='report_stocks'),


    path('register/<int:inquiryid>/', views.register, name='register'),
    path('viewing-pic/valid-id/<int:id>/', views.viewpic_vid , name='viewingpic_vid'),	
    path('viewing-pic/business-permit/<int:id>/', views.viewpic_bpermit , name='viewingpic_bpermit'),	

    #settings profile 
    path('settings_profile/', views.settings_profile, name='settings_profile'),
    path('settings_password/', views.settings_password, name='settings_password'),

    #view
    path('settings_product/', views.settings_product, name='settings_product'),
    # path('settings_add/', views.settings_addproduct, name='settings_addproduct'),

    #add 	
    path('add-category/', views.settings_addcategory , name='settings_addcategory'),	
    path('add-unit/', views.settings_addunit , name='settings_addunit'),	
    path('add-flavor/', views.settings_addflavor , name='settings_addflavor'),

    #remove
    # path('remove-settings_product/<int:id>/', views.settings_remove, name='settings_remove'),
    path('remove/Product-category/<int:id>/', views.remove_category , name='remove_category'),	
    path('remove/Product-unit/<int:id>/', views.remove_unit , name='remove_unit'),	
    path('remove/Product-flavor/<int:id>/', views.remove_flavor , name='remove_flavor'),

    #return products	
    # path('Return/Product/', views.return_product, name='return_product'),

    path('unreturned/Product/', views.unreturned_product, name='unreturned_product'),
    path('returned/Product/', views.returned_product, name='returned_product'),
    path('returned/completed/<int:id>/', views.returned_completed, name='returned_completed'),
    path('view-unreturned/<int:id>/', views.view_unreturned, name='view_unreturned'),
    path('view-returned/<int:id>/', views.view_unreturned, name='view_unreturned'),


    path('Add/Return-Product/', views.add_returnproduct , name='add_returnproduct'),
    path('edit/Return-Product/<int:id>/', views.edit_returnproduct , name='edit_returnproduct'),	
    path('update/Return-Product/<int:id>/', views.update_returnproduct , name='update_returnproduct'),
    

    path('support/', views.support, name='support'),
   
#    settings for visitor's page
    path('settings_content/', views.settings_page, name='settings_page'),

]