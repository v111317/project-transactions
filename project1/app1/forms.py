from django import forms

class InputForm(forms.Form):
    transaction_type = forms.CharField(label="Transaction Type")
    amount = forms.CharField(label="Amount")
    description = forms.CharField(label="Description")