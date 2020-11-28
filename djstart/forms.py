from django import forms

class DjstartForm(forms.Form):
    check = forms.NullBooleanField(label='Check')