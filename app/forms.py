import os
from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    sender = forms.CharField()
    sender_email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        sender = self.cleaned_data["sender"]
        sender_email = self.cleaned_data["sender_email"]
        phone = self.cleaned_data["phone"]
        message = self.cleaned_data["message"]
        subject = "Portfolio Contact"
        body = """Hey you got an email regarding your portfolio!
               From: {}
               Email: {}
               Phone Number: {}
               Message: {}
               """.format(sender, sender_email, phone,  message)
        recipient_list = [os.environ.get("EMAIL_HOST_USER")]
        # print(recipient_list)
        send_mail(subject, body, sender, recipient_list)
