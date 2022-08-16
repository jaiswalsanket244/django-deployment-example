from django.contrib.auth.models import User
from my_app.models import UserinfoModel
from django import forms

class User_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class User_profile_info_form(forms.ModelForm):
    class Meta():
        model = UserinfoModel
        fields = ('portfolio_site_model','portfolio_pic_model')
        
