from django.shortcuts import render, redirect
from admin_site.models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q


# Create your views here.
def dashboard(request):
    list_pending = Transaction.objects.filter(transaction_orderstatus = "Out for Delivery").count()
    list_complete = Transaction.objects.filter(transaction_orderstatus = "Completed").count()
    list_profile = Profile.objects.filter(list_user = request.user)
    current_profile = Profile.objects.filter(list_user = request.user)

    context ={
        'list_pending':list_pending,
        'list_complete':list_complete,
        'sidebar' : 'riderdashboard',
        'list_profile': list_profile,
        'current_profile':current_profile,
    }
    return render(request, 'rider_site/dashboard/index.html', context)

# @login_required(login_url='landing_page:login')
# def deliver_orders(request):
#     status = "Out for Shipping"
#     list_transaction = Transaction.objects.filter(transaction_orderstatus = status)
#     context = {
#         'list_transaction': list_transaction
#     }
#     return render(request, 'rider_site/deliver_orders/deliver_orders.html', context)

@login_required(login_url='landing_page:login')
def orders_completed(request, orderid):
    if request.method == "POST":
        transaction = Transaction.objects.get(id = orderid)
        now = datetime.now()
        status = "Completed"
        activity = "Delivered"
        transaction.transaction_delivered = now
        transaction.transaction_orderstatus = status
        transaction.save()
        
        NewActLog = Activity_log()
        NewActLog.user_name = request.user
        NewActLog.activity = activity 
        NewActLog.role = request.user.role
        NewActLog.date_time = now
        NewActLog.save()


        messages.success(request, ("Successfully Delivered"))
        return redirect('rider_site:transaction_orders')


@login_required(login_url='landing_page:login') 
def transaction_orders(request):
    status = "Out for Delivery"
    current_profile = Profile.objects.filter(list_user = request.user)
    list_profile = Profile.objects.filter(list_user = request.user)
    list_transaction = Transaction.objects.filter(Q(transaction_orderstatus = status) & Q(transaction_doption = "delivery")).order_by('-id')
    context = {
        'list_transaction':list_transaction,
        'sidebar' : 'riderorders',
        'list_profile': list_profile,
        'current_profile':current_profile,
    }
    return render(request, 'rider_site/orders/index.html', context)

@login_required(login_url='landing_page:login') 
def transaction_view(request,id):
    if request.method == "GET":
        transaction = Transaction.objects.get(id = id)

        transaction_no = transaction.transaction_no
        list_orderitem = OrderItem.objects.filter(OrderItem_transactionNo = transaction_no).order_by('-id')

        list_total = OrderItem.objects.filter(OrderItem_transactionNo = transaction_no).all().aggregate(data=Sum('OrderItem_amount'))

        context = {
            'list_orderitem':list_orderitem,
            'list_total':list_total,
            'list_transaction':transaction
        }
        
    return render(request, 'rider_site/orders/view_orders.html', context)

@login_required(login_url='landing_page:login')
def completed_process(request):
    if request.method == "POST":
        transaction_no = request.POST['transaction_no']
        now = datetime.now()
        transaction = Transaction.objects.get(transaction_no = transaction_no)
        transaction.transaction_orderstatus = "Completed"
        transaction.transaction_delivered = now
        transaction.save()

        activity = "Delivered"
        NewActLog = Activity_log()
        NewActLog.user_name = request.user
        NewActLog.activity = activity 
        NewActLog.role = request.user.role
        NewActLog.date_time = now
        NewActLog.save()
        messages.success(request,("Successfully Delivered"))
        return redirect('rider_site:transaction_orders')



@login_required(login_url='landing_page:login')
def report_deliver(request):
    list_profile = Profile.objects.filter(list_user = request.user)
    list_transaction = Transaction.objects.filter(transaction_orderstatus = "Completed").order_by('-id')
    current_profile = Profile.objects.filter(list_user = request.user)
    context = {
        'list_transaction':list_transaction,
        'sidebar' : 'riderreport',
        'list_profile': list_profile,
        'current_profile':current_profile,
    }
    return render(request, 'rider_site/report/index.html',context)







