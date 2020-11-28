from django import forms

class DjstartForm(forms.Form):
   data = [
       ('one','item1'),
       ('two','item2'),
       ('three','item3')    
   ]
   choice = forms.ChoiceField(label='Choice',choices=data)