from django import forms

class ContactForm(forms.Form):
	Email = forms.EmailField(widget=forms.EmailInput())
	Titulo = forms.CharField(widget=forms.TextInput())
	Texto = forms.CharField(widget=forms.Textarea())
    # TODO: Define form fields here
    