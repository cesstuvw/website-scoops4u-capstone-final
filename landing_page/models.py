from django.db import models
from django.contrib.auth.models import AbstractUser
# from admin_site.models import Review


# Create your models here.

class User(AbstractUser):
    ROLE = ((" "," "),("admin","admin"),("si_staff","si_staff"),("reseller","reseller"),("delivery_staff","delivery_staff"))  
    STAT = ((" "," "),("active","active"),("inactive","inactive"))
    role = models.CharField(max_length=50, null=True, default=None, choices=ROLE)
    status = models.CharField(max_length=50, null=True, default=None , choices=STAT)



# class Review(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email_address = models.EmailField(max_length=50)
#     star_rating = models.CharField(max_length=50)
#     review = models.CharField(max_length=500)