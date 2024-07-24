from django import forms
from .models import MoneyControl

class MoneyControlForm(forms.ModelForm):
    class Meta:
        model = MoneyControl
        fields = ['date', 'type', 'amount', 'account', 'category', 'description']

