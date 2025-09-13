from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = ['name', 'email', 'message']
        fields = '__all__'


# class SubscriptionForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     email = forms.EmailField()