from django.forms import forms

class GoogleBookForm(forms.Form):
    search_terms = forms.Field(label='Search item', required=True)