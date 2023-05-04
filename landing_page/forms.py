from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':"username",
            'id':'username',
            'type':'text',
            # 'placeholder':'username',
            'maxlength':'25',
            'minlength':'6'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':'email',
            'id':'email',
            'type':'email',
            # 'readonly':'readonly',
            # 'placeholder':'enter email',
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':"password1",
            'id':'password1',
            'type':'password',
            # 'placeholder':'password',
            'maxlength':'40',
            'minlength':'6'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':"password2",
            'id':'password2',
            'type':'password',
            # 'placeholder':'re-enter password',
            'maxlength':'40',
            'minlength':'6'
        })

        self.fields['role'].widget.attrs.update({
            'class': 'form-select',
        })

        self.fields['status'].widget.attrs.update({
            'class': 'form-select',
        })


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already exists.")
        return email
            

    class Meta:
        model = User
        fields = ('username','email','password1','password2','role','status')
    
    
class ChangePasswordForm(forms.Form):
    # current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput)
    current_password = forms.CharField(label='Current Password',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    # myfield = forms.CharField(widget=forms.TextInput)


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email_address = forms.EmailField(max_length = 150, widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    message = forms.CharField(widget = forms.Textarea(attrs={'rows': '3', 'class' : 'form-control'}), max_length = 2000)


class ReviewForm(forms.Form):
    CHOICES = [
        ('0', ''),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    first_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email_address = forms.EmailField(max_length = 150, widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    star_rating = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-select'}), choices=CHOICES)
    review = forms.CharField(widget = forms.Textarea(attrs={'rows': '3', 'class' : 'form-control'}), max_length = 2000)


# class StoreSettingsForm(forms.Form):
#     name_store = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     address_store = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))

