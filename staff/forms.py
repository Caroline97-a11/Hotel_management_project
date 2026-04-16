from django import forms
from .models import Staff
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class StaffForm (UserCreationForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'roles','username','password1', 'password2']
class StaffLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please enter user name'}),
        error_messages= {'required': 'This field can not be empty!'}
    
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter password'}),
        error_messages={'required': 'please enter your password!'}
    )