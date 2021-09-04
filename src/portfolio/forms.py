from django import forms

class ContactForm (forms.Form):
    name = forms.CharField(
        label='Name', 
        max_length=250, 
        widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(
        label='Email', 
        max_length=250, 
        widget=forms.EmailInput(attrs={'class': 'input'}))
    msg = forms.CharField(
        label='Message', 
        max_length=1000, 
        widget=forms.Textarea(attrs={'class': 'input'}))
