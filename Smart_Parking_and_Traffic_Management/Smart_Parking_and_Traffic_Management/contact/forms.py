from django import forms
from .models import CustomerEnquiry

class CustomerEnquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerEnquiry
        fields = ['name', 'email', 'subject', 'message']
