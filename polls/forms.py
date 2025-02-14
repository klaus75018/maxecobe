from django import forms

class ContactForm(forms.Form):
    message = forms.CharField(label="Votre message",widget=forms.Textarea())
    #Password = forms.PasswordInput()