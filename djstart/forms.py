from django import forms

class DjstartForm(forms.Form):
    id = forms.IntegerField(label='ID')