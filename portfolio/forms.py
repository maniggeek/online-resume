from django import forms

class ContactForm(forms.Form):
    Email = forms.EmailField(required=True)
    Subject = forms.CharField(required=True)
    Message = forms.CharField(widget=forms.Textarea, required=True)
