from django import forms
from .models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

        widgets = {
            'date_registered': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }

        error_messages = {
            'first_name': {
                'required': 'Please enter your first name'
            },
            'last_name': {
                'required': 'Please enter your last name'
            },
            'phone_number': {
                'required': 'Please enter a valid phone number'
            },
            'email': {
                'required': 'Please enter a correct email'
            },
            'date_registered': {
                'required': 'Please enter a correct date'
            },
            'guest_status': {
                'required': 'Please enter your status'
            },
        }
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if len(first_name) < 2:
            raise forms.ValidationError('The name is invalid, please enter a valid name')

        return first_name