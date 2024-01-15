from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }