from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from .models import *
from admin_site.models import *

from django.core.mail import send_mail, BadHeaderError, EmailMessage
from .forms import ContactForm, ReviewForm 

from django.urls import reverse

# Create your views here.
# home
def landing_page(request):
    reviews = Review.objects.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            subject = "Review"
            email = form.cleaned_data['email_address']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            rating = form.cleaned_data['star_rating']
            review = form.cleaned_data['review']
            message = f"Email: {email} \n\n" \
                    f"First Name: {first_name}\n" \
                    f"Last Name: {last_name}\n" \
                    f"Rating: {rating}\n" \
                    f"Review: {review}\n"

            email_msg = EmailMessage(
                subject=subject,
                body=message,
                from_email=email,
                to=['blubirdmailbox@gmail.com'],
                reply_to=[email]
            )

            try: 
                email_msg.send()
                messages.success(request,("Review sent"))

                # Send automatic reply
                automatic_reply_subject = "Thank you for your review of our ice cream and service!"
                automatic_reply_message = f"Hello {first_name},\n\n" \
                                        f"Thank you for taking the time to review our ice cream. We truly appreciate your feedback and are delighted to hear that you enjoyed your experience with us.\n\n" \
                                        f"Our team is always striving to improve, so please don't hesitate to reach out if you have any further comments or suggestions.\n\n" \
                                        f"Thanks again for choosing our ice cream!\n\n" \
                                        f"Best regards,\n\n" \
                                        f"Owner\n" \
                                        f"SCOOPS 4 U"
                automatic_reply = EmailMessage(automatic_reply_subject, automatic_reply_message, 'blubirdmailbox@gmail.com', [email])
                automatic_reply.reply_to = ['blubirdmailbox@gmail.com']
                automatic_reply.send(fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                
            url = reverse('landing_page:landing_site') + '#feedbacks'
            return redirect(url)

    form = ReviewForm()
    return render(request, 'landing_page/index.html', {'form': form, 'menu': 'home'})


# flavors
def flavors(request):
    return render(request, 'landing_page/flavors.html', {'menu': 'flavors'})

# about
def about(request):
    return render(request, 'landing_page/about.html', {'menu': 'about'})

# contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Question"
            email = form.cleaned_data['email_address']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            ques = form.cleaned_data['message']
            message = f"Email: {email}\n\n" \
                    f"First Name: {first_name}\n" \
                    f"Last Name: {last_name}\n" \
                    f"Question: {ques}\n"

            email_msg = EmailMessage(
                subject=subject,
                body=message,
                from_email=email,
                to=['blubirdmailbox@gmail.com'],
                reply_to=[email]
            )

            try: 
                email_msg.send()
                messages.success(request,("Question sent"))

                # Send automatic reply
                automatic_reply_subject = "Thank you for your inquiry"
                automatic_reply_message = f"Dear {first_name},\n\nThank you for contacting us. We have received your inquiry and a member of our team will get back to you as soon as possible. We appreciate your interest in our brand and look forward to assisting you.\n\nBest regards,\n\nOwner\nSCOOPS 4 U"
                automatic_reply = EmailMessage(automatic_reply_subject, automatic_reply_message, 'blubirdmailbox@gmail.com', [email])
                automatic_reply.reply_to = ['blubirdmailbox@gmail.com']
                automatic_reply.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('/contact#question')

    form = ContactForm()
    
    return render(request, 'landing_page/contact.html', {'form': form, 'menu': 'contact'})

# be-a-reseller
def reseller(request):
    return render(request, 'landing_page/be-a-reseller.html', {'menu': 'reseller'})



# first landing of page
# def landing_page(request):
#     return render(request, 'landing_page/index.html')


# login process for multi user
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =  authenticate(request,username=username, password=password)
        activity = "signed-in"
    
        if user is not None:
            # current_user =  User.objects.get(pk=user.pk)
            login(request, user)  

            #activity log for login
            activity = "Signed-in"
            NewActLog = Activity_log()
            NewActLog.user_name = request.user
            NewActLog.role = request.user.role
            NewActLog.activity = activity 
            NewActLog.save()
    

            if user.role == "admin" and user.status == "active": 
                return redirect('admin_site:dashboard') 
            elif user.role == "reseller" and user.status == "active":
                return redirect('reseller_site:dashboard')
            elif user.role == "delivery_staff" and user.status == "active":    
                return redirect('rider_site:dashboard')
            elif user.role == "si_staff" and user.status == "active": 
                return redirect('staff_site:dashboard')
            elif user.status == "inactive": 
                messages.error(request, ("Your account is no longer active"))
                return redirect('landing_page:login') 
            else: 
                messages.error(request, ("Wrong Username and Password"))
                return redirect('landing_page:login') 

        else:
            messages.error(request, ("Wrong Username and Password"))
            return redirect('landing_page:login') 
    
    return render(request, 'landing_page/login-folder/login.html')




    
@login_required(login_url='landing_page:login')
def logoutView(request):
    
    #activity log for login
    activity = "Signed-out"
    NewActLog = Activity_log()
    NewActLog.user_name = request.user
    NewActLog.role = request.user.role
    NewActLog.activity = activity 
    NewActLog.save()

    logout(request)
    return render(request, 'landing_page/login-folder/login.html')



       





# def loginView(request):
#     # current_user =  User.objects.get(pk=user.pk)
#     if request.method == 'POST':
#         username= request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
   
#         if user is not None and user.role == "admin":
#             login(request, user)
#             return redirect('landing_page:dashboard_admin')
#         elif user is not None and user.role == "reseller":
#             login(request, user)
#             return redirect('landing_page:dashboard_staff') 
#         elif user is not None and user.role == "staff":
#             login(request, user)
#             return redirect('landing_page:dashboard_staff')
#         elif user is not None and user.role == "delivery_staff":
#             login(request, user)
#             return redirect('scoops_admin:list_reseller')  
#         else:
#             messages.success(request, ("There Was An Error Logging In, Try Again ..."))
#             return render(request,'landing_page/login-folder/login.html') 
#     else:
#         return render(request, 'landing_page/login-folder/login.html')    

# logout session here.

# for inquiry here.
def inquiry_reseller(request):
    return render(request, 'landing_page/inquiry_reseller.html')    


# dashboard for admin_site.



# dashboard for staff_site.

# def review_list(request):
#     reviews = Review.objects.all()
#     return render(request, 'index.html', {'reviews': reviews})
 

    