from django import forms

class PredictionForm(forms.Form):
    numbers = forms.IntegerField(label='رقمك')
    something = forms.IntegerField(label='اي شيء')
