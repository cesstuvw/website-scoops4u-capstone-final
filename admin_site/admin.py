from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Scooups4U"
admin.site.site_title ="Scoops4U Admin Area"
admin.site.index_title ="Welcome to the Scoops4u Admin Area"



class ResellerView(admin.ModelAdmin):
    list_display = ['reseller_fname', 'reseller_mname', 'reseller_lname', 'reseller_gender','reseller_contact','reseller_address','reseller_email','reseller_id','reseller_businessp','reseller_status']
    search_fields = ['reseller_fname','reseller_mname','reseller_lname','reseller_status']
class ProductView(admin.ModelAdmin):
    list_display = ['product_code',  'product_name','product_category', 'product_unit','product_ResellerPrice','product_price','product_stock','product_status']
    search_fields = ['product_code', 'product_category', 'product_name', 'product_unit','product_ResellerPrice','product_price','product_stock','product_status']

# class SettingsView(admin.ModelAdmin):
#     list_display = ['settings_category','settings_unit']
#     search_fields = ['settings_category','settings_unit']

class BatchView(admin.ModelAdmin):
    list_display = ['product_code','product_name','product_batch','product_quantity','product_expired','created_at']
    search_fields = ['product_code','product_name', 'product_batch','product_quantity','product_expired','created_at']
class CartView(admin.ModelAdmin):
    list_display = ['cart_user','cart_pcode', 'cart_category', 'cart_name', 'cart_unit','cart_reseller_price','cart_price','cart_quantity','cart_amount']
    search_fields = ['cart_user','cart_pcode', 'cart_category', 'cart_name', 'cart_unit','cart_reseller_price','cart_price','cart_quantity''cart_amount']

class Cart_PaymentView(admin.ModelAdmin):
    list_display = ['cart_user', 'pos_number','cart_TotalAmount','cart_cash','cart_change','cart_status','cart_date']
    search_fields =  ['cart_user','cart_TotalAmount','cart_cash','cart_change','cart_status','cart_date']

class TransactionView(admin.ModelAdmin):
    list_display = ['transaction_no','transaction_user','transaction_fname','transaction_lname','transaction_address','transaction_contactno','transaction_totalprice','transaction_doption','created_at','transaction_preferred_date','transaction_delivered','transaction_orderstatus']
    search_fields = ['transaction_no','transaction_user','transaction_fname','transaction_lname','transaction_address','transaction_contactno','transaction_doption','transaction_preferred_date','transaction_totalprice','created_at','transaction_delivered','transaction_orderstatus']

class OrderItemView(admin.ModelAdmin):
    list_display = ['OrderItem_transactionNo', 'OrderItem_category', 'OrderItem_name', 'OrderItem_unit','OrderItem_quantity','OrderItem_amount']
    search_fields =  ['OrderItem_transactionNo', 'OrderItem_category', 'OrderItem_name', 'OrderItem_unit','OrderItem_quantity','OrderItem_amount']

class ProfileView(admin.ModelAdmin):
    list_display = ['list_user','profile_fname', 'profile_mname', 'profile_lname', 'profile_cnumber','profile_address','profile_email','profile_pic']
    search_fields = ['list_user','profile_fname', 'profile_mname', 'profile_lname', 'profile_cnumber','profile_address','profile_email']


class Activity_logView(admin.ModelAdmin):
    list_display = ['user_name','activity','role','date_time']
    search_fields = ['user_name','activity','role','date_time']








admin.site.register(Reseller, ResellerView),
admin.site.register(Product, ProductView),
admin.site.register(By_Batch, BatchView),
admin.site.register(Cart, CartView),
admin.site.register(Transaction, TransactionView),
admin.site.register(OrderItem, OrderItemView),
admin.site.register(Activity_log, Activity_logView),
admin.site.register(Profile, ProfileView),
admin.site.register(Cart_Payment, Cart_PaymentView),
# admin.site.register(Settings,SettingsView),
admin.site.register(Return_product),	
admin.site.register(Settings_category),	
admin.site.register(Settings_unit),	
admin.site.register(Settings_flavor),