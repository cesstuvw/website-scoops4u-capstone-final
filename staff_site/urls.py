from django.urls import path
from staff_site import views

app_name = 'staff_site'
urlpatterns = [
    path('', views.dashboard, name='dashboard')
]