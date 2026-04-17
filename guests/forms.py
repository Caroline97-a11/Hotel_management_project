from django import forms
from .models import Guest
import re

class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'email': 'Email Address',
            'date_registered': 'Date of Registration',
            'guest_status': 'Guest Status',
            'room_number': 'Room Number',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+2567XXXXXXXX'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@gmail.com'
            }),

            'date_registered': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'guest_status': forms.Select(attrs={
                'class': 'form-control'
            }),

            'room_number': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise forms.ValidationError('Please enter your last name')

        if not re.match("^[A-Za-z]+$", last_name):
            raise forms.ValidationError("The name should contain only alphabets")

        return last_name

    def clean_phone_number(self):
            phone = self.cleaned_data['phone_number']

            pattern = r'^\+2567\d{8}$'

            if not re.match(pattern, phone):
                raise forms.ValidationError(
                    "Phone number must start with +2567 "
                )
            if len(phone)!=13:
                raise forms.ValidationError('Phone number should not exceed 13 digits')

            return phone
            