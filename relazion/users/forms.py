from django import forms
from .models import Users,Messages

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['names','birth','sex','color','height','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['id','password']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['id_sender','id_receiver','message']