from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['names','birth','sex','color','height','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['id','password']