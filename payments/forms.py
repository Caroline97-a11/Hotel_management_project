from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        if not amount:
            raise forms.ValidationError("Amount is required")

        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than 0")

        return amount