from django.shortcuts import render, redirect
from admin_site.models import *
from django.db.models import Sum,Q,F, Max	
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random, locale
from decimal import Decimal




# Create your views here.
@login_required(login_url='landing_page:login')
def dashboard(request):
    list_numberorder =    Transaction.objects.filter(transaction_user = request.user).count()
    transaction_pending = Transaction.objects.filter(transaction_user = request.user,transaction_orderstatus = "Pending").count()
    transaction_shipped = Transaction.objects.filter(transaction_user = request.user,transaction_orderstatus = "Out for Delivery").count()
    transaction_decline = Transaction.objects.filter(transaction_user = request.user,transaction_orderstatus = "Decline").count()
    list_profile = Profile.objects.filter(list_user = request.user)
    current_profile = Profile.objects.filter(list_user = request.user)

    context={
        'list_numberorder':list_numberorder,
        'transaction_pending':transaction_pending,
        'transaction_shipped':transaction_shipped,
        'transaction_decline':transaction_decline,
        'sidebar':'resdashboard',
        'list_profile': list_profile,
        'current_profile':current_profile,
    }
    return render(request, 'reseller_site/dashboard/index.html',context)

# @login_required(login_url='landing_page:login')
# def orders_reseller(request):
#     list_transaction = Transaction.objects.filter(transaction_user = request.user).order_by('-id')
#     context = {
#         'list_transaction':list_transaction
#     }
#     return render(request, 'reseller_site/orders/orders.html',context)

@login_required(login_url='landing_page:login')
def cart_reseller(request):
    list_profile = Profile.objects.filter(list_user = request.user)
    total_item = Cart.objects.filter(cart_user = request.user).count()
    list_cart = Cart.objects.filter(cart_user = request.user).order_by('-id')
    sum_amount = Cart.objects.filter(cart_user = request.user).aggregate(sum_amount =Sum('cart_ResellerAmount'))['sum_amount']
    cart = Cart.objects.filter(cart_user = request.user)	
    current_profile = Profile.objects.filter(list_user = request.user)
    times_amount = None
    if Cart.objects.filter(cart_user = request.user):
        for carts in cart:     	
            products = Product.objects.get(product_code = carts.cart_pcode)	
            if products.product_stock < carts.cart_quantity:	
                messages.error(request,("Some Product out of stock"))	
                return redirect('reseller_site:add_cart')
                
    if sum_amount >= 5000:
        times_amount = int(sum_amount) * 0.02
    else:
        times_amount = 0
        



    # promo = Promo.objects.get(promo_amount =sum_amount)

    # if sum_amount >= 5000:
    #     promo = 100
        
    # elif



    

    context = {
        'list_cart':list_cart,
        'sum_amount':sum_amount,
        'total_item':total_item,
        'promo':times_amount,
        'list_profile': list_profile,
        'current_profile':current_profile,

    }
    return render(request, 'reseller_site/cart/checkout.html', context)

@login_required(login_url='landing_page:login')
def minus_qty(request, productid):
    pos = Cart.objects.get(id =productid)
    if pos.cart_quantity == 1:	
        pos.delete()
        return redirect('reseller_site:add_cart')
    else:


        current_qty = int(pos.cart_quantity)
        result = current_qty - 1
        pos.cart_quantity = result
        pos.save()

        current_amount = int(pos.cart_ResellerAmount)
        current_price = int(pos.cart_reseller_price )
        result = current_amount - current_price
        pos.cart_ResellerAmount = result
        pos.save()
    
        current_pcode = pos.cart_pcode
        # product = Product.objects.get(product_code = current_pcode)
        # current_stock = int(product.product_stock)
        # retrieve_stock = current_stock + 1
        # product.product_stock = retrieve_stock
        # product.save()

        # if product.product_stock > 0:	
        #     product.product_status = "available"	
        #     product.save()
        return redirect('reseller_site:add_cart')


@login_required(login_url='landing_page:login')
def add_qty(request,productid):
        pos = Cart.objects.get(id =productid)
        current_qty = int(pos.cart_quantity)
        result = current_qty + 1

        #for checking product code
        current_pcode = pos.cart_pcode

        product = Product.objects.get(product_code = current_pcode)
        if product.product_stock == 0:
            messages.success(request,("No available Stock"))
            return redirect('reseller_site:add_cart')

        elif product.product_stock <= pos.cart_quantity:	
            messages.error(request,('The available stock is not enough'))	
            return redirect('reseller_site:add_cart')

        else:
            pos.cart_quantity = result
            pos.save()

            current_amount = int(pos.cart_ResellerAmount)
            current_price = int(pos.cart_reseller_price)
            result = current_amount + current_price
            pos.cart_ResellerAmount = result
            pos.save()



        return redirect('reseller_site:add_cart')

@login_required(login_url='landing_page:login')
def checkout(request):
    if request.method == "POST":
        current_user = request.user
        pos = Cart.objects.filter(cart_user = current_user)
        preferred_date = request.POST['prefer_date']
        no_specific = "None"
        status = "Pending"
        trackno = 'S4U'+str(random.randint(1111111, 9999999))
        if preferred_date:
            NewTransaction = Transaction()
            NewTransaction.transaction_user = request.user
            NewTransaction.transaction_fname = request.POST.get('fname')
            NewTransaction.transaction_lname = request.POST.get('lname')
            NewTransaction.transaction_address = request.POST.get('address')
            NewTransaction.transaction_contactno= request.POST.get('contact_no')
            NewTransaction.transaction_doption = request.POST.get('option')
            NewTransaction.transaction_preferred_date = preferred_date 
            NewTransaction.transaction_totalprice = int(request.POST.get('total_amount'))
            NewTransaction.transaction_orderstatus = status

        
            while Transaction.objects.filter(transaction_no = trackno) is None:
                trackno = 'S4U'+str(random.randint(1111111,9999999))

            NewTransaction.transaction_no = trackno   
            NewTransaction.save()

            #activity log for Checkout
            activity = "Check-out"
            NewActLog = Activity_log()
            NewActLog.user_name = request.user
            NewActLog.role = request.user.role
            NewActLog.activity = activity 
            NewActLog.save()
        

            NewOrderItems = Cart.objects.filter(cart_user = request.user)
            for item in NewOrderItems:
                OrderItem.objects.create(
                    OrderItem_transactionNo = trackno,
                    OrderItem_name = item.cart_name,
                    OrderItem_flavor = item.cart_flavor,
                    OrderItem_category = item.cart_category,
                    OrderItem_unit = item.cart_unit,
                    OrderItem_quantity  = item.cart_quantity,
                    OrderItem_amount= item.cart_amount
                )

            if Cart.objects.filter(cart_user = request.user):	
                for carts in pos:	
                    products = Product.objects.get(product_code = carts.cart_pcode)	
                    cart_quantity = int(carts.cart_quantity)	
                    current_stock = int(products.product_stock)	
                    minus_stock =  current_stock - cart_quantity	
                    products.product_stock = minus_stock	
                    products.save()	
                    if products.product_stock == 0:	
                        products.product_status = "not available"	
                        products.save()	
                    elif products.product_stock <= 20:	
                        products.product_status = "low stock"	
                        products.save()
                pos.delete()	
                messages.success(request, ("Please wait for your order"))	
                return redirect('reseller_site:transaction_orders')
        else:
            NewTransaction = Transaction()
            NewTransaction.transaction_user = request.user
            NewTransaction.transaction_fname = request.POST.get('fname')
            NewTransaction.transaction_lname = request.POST.get('lname')
            NewTransaction.transaction_address = request.POST.get('address')
            NewTransaction.transaction_contactno= request.POST.get('contact_no')
            NewTransaction.transaction_doption = request.POST.get('option')
            NewTransaction.transaction_preferred_date = no_specific
            NewTransaction.transaction_totalprice = request.POST.get('total_amount')
            NewTransaction.transaction_orderstatus = status

        
            while Transaction.objects.filter(transaction_no = trackno) is None:
                trackno = 'S4U'+str(random.randint(1111111,9999999))

            NewTransaction.transaction_no = trackno   
            NewTransaction.save()


            #activity log for Checkout
            activity = "Check-out"
            NewActLog = Activity_log()
            NewActLog.user_name = request.user
            NewActLog.role = request.user.role
            NewActLog.activity = activity 
            NewActLog.save()
        

            NewOrderItems = Cart.objects.filter(cart_user = request.user)
            for item in NewOrderItems:
                OrderItem.objects.create(
                    OrderItem_transactionNo = trackno,
                    OrderItem_name = item.cart_name,
                    OrderItem_flavor = item.cart_flavor,
                    OrderItem_category = item.cart_category,
                    OrderItem_unit = item.cart_unit,
                    OrderItem_quantity  = item.cart_quantity,
                    OrderItem_amount= item.cart_ResellerAmount
                )

                if Cart.objects.filter(cart_user = request.user):	
                    for carts in pos:	
                        products = Product.objects.get(product_code = carts.cart_pcode)	
                        cart_quantity = int(carts.cart_quantity)	
                        current_stock = int(products.product_stock)	
                        minus_stock =   current_stock - cart_quantity	
                        products.product_stock = minus_stock	
                        products.save()
                    
                        if products.product_stock == 0:	
                            products.product_status = "not available"	
                            products.save()	
                        elif products.product_stock <= 20:	
                            products.product_status = "low stock"	
                            products.save()
                pos.delete()
            messages.success(request, ("Please wait for your order"))
            return redirect('reseller_site:transaction_orders')


@login_required(login_url='landing_page:login') 
def transaction_orders(request):
    list_transaction = Transaction.objects.filter(transaction_user= request.user).order_by('-id')
    list_profile = Profile.objects.filter(list_user = request.user)
    current_profile = Profile.objects.filter(list_user = request.user)

    context = {
        'list_transaction':list_transaction,
        'sidebar':'resorders',
        'list_profile': list_profile,
        'current_profile':current_profile,
    }
    return render(request, 'reseller_site/orders/orders.html', context)


#list reseller cart
@login_required(login_url='landing_page:login')
def add_cart(request):
    list_profile = Profile.objects.filter(list_user = request.user)
    list_products = Product.objects.all()
    current_user = request.user
    current_profile = Profile.objects.filter(list_user = request.user)
    list_pos = Cart.objects.filter(cart_user = current_user).order_by('-id')
    sum_amount = Cart.objects.filter(cart_user = current_user).all().aggregate(total =Sum('cart_ResellerAmount'))['total']
    

    context = {
        'list_products':list_products,
        'list_pos':list_pos,
        'sum_amount':sum_amount,
        'list_profile': list_profile,
        'current_profile':current_profile,
        }
    return render(request, 'reseller_site/cart/cart.html', context)

@login_required(login_url='landing_page:login')
def all_products(request):
    list_products = Product.objects.all()
    context = {'list_products':list_products}
    return render(request, 'reseller_site/cart/all-products.html', context)

@login_required(login_url='landing_page:login')
def cart_products(request, productid):
    if request.method =="POST":
        # getting id 
       
        product = Product.objects.get(id = productid)
        
       

        # coming from  input type
        qty = int(request.POST['quantity'])
        p_stock = int(request.POST['stock'])
        pcode = request.POST['product_code']
        p_reseller_price = float(request.POST['product_reseller_price'])
        p_price = float(request.POST['product_price'])
        p_unit = request.POST['product_unit']
        p_category = request.POST['product_category']
        p_name = request.POST['product_name']
        p_flavor = request.POST['product_flavor']	

       
         
        # session,  getting  user name
        current_user = request.user
        
        # minus or adding to the stock
        # diff = p_stock -  qty 
        amount_cart = p_price * qty
        reseller_cart = p_reseller_price * qty
        
        #converting the data of product stock to integer
        avail_stock = int(product.product_stock)

        #checking if have already product in the cart

        status = "low stock"

        
        

        # error trapping for 0 stock    
        if Cart.objects.filter(cart_user=request.user, cart_pcode = pcode):
            messages.error(request,("you already have on the cart"))
            return redirect('reseller_site:add_cart')
        elif  product.product_stock == 0:
            messages.error(request,("Sorry, No Available Stock"))
            return redirect('reseller_site:add_cart')

        # error trapping for low stock
        elif avail_stock <  qty:
            messages.error(request,("sorry available stock are not enough"))
            return redirect('reseller_site:add_cart')
        elif product.product_status =="not available":
            messages.error(request,("Sorry, this Product is not Available"))
            return redirect('reseller_site:add_cart')      
        else:

            #updating product stock
            # product.product_stock = diff
            # product.save()

            #inserting product in pos table
            pos = Cart(cart_user=current_user, cart_pcode=pcode, cart_flavor= p_flavor, cart_category= p_category,  cart_name = p_name, cart_unit= p_unit,cart_reseller_price =p_reseller_price , cart_price = p_price, cart_quantity = qty, cart_amount = amount_cart,  cart_ResellerAmount =reseller_cart )
            pos.save()	
            if product.product_stock == 0:	
                product.product_status = "not available"	
                product.save() 
            
            
            messages.success(request,("Successfully carting Products"))
            return redirect('reseller_site:add_cart') 

@login_required(login_url='landing_page:login') 
def transaction_view(request,id):

    if request.method == "GET":
        transaction = Transaction.objects.get(id = id)

        transaction_no = transaction.transaction_no
        list_orderitem = OrderItem.objects.filter(OrderItem_transactionNo = transaction_no).order_by('-id')

        list_total = OrderItem.objects.filter(OrderItem_transactionNo = transaction_no).aggregate(data=Sum('OrderItem_amount'))['data']

        context = {
            'list_orderitem':list_orderitem,
            'list_total':list_total,
            'list_transaction':transaction
        }
    
    return render(request, 'reseller_site/orders/view_orders.html', context)




@login_required(login_url='landing_page:login')
def cart_cancel(request,productid):
    if request.method == "POST":
        cancel = Cart.objects.get(id =productid)
        # current_pcode = request.POST['current_pcode']
        # product = Product.objects.get(product_code = current_pcode)

        # current_qty = int(request.POST['current_qty'])
        # current_stock = int(product.product_stock)

        # return_stock = current_stock + current_qty
        # product.product_stock = return_stock
        # product.save()
        cancel.delete()

        #activity log for cancelling the product
        activity = "Cancelled Cart"
        NewActLog = Activity_log()
        NewActLog.user_name = request.user
        NewActLog.role = request.user.role
        NewActLog.activity = activity 
        NewActLog.save()

        #removing in pos payment
        # pos_id = request.POST['pos_id']
        pos_payment = Cart_Payment.objects.filter(cart_user =request.user.role, cart_status="not Print")
        pos_payment.delete()

        # if product.product_stock != 0:	
        #     product.product_status = "available"	
        #     product.save()
    

        
        messages.success(request,("Successfully cancelled"))
        return redirect('reseller_site:add_cart')

def cart_removeall(request):	
    pos = Cart.objects.filter(cart_user = request.user)	
    pos.delete()	
    messages.success(request,("successfully removed all"))	
    return redirect('reseller_site:add_cart')	


