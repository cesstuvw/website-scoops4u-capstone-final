from django.urls import path
from rider_site import views

app_name = 'rider_site'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('orders-reseller', views.deliver_orders, name='deliver_orders'),
    path('orders-completed/<int:orderid>/', views.orders_completed, name='orders_completed'),
    path('transaction-orders/process-completed', views.completed_process, name='completed_process'),


    path('report-deliver/', views.report_deliver, name='report_deliver'),

    path('orders/', views.transaction_orders, name='transaction_orders'),
    path('transaction-view/<int:id>/', views.transaction_view, name='transaction_view'),
   
]