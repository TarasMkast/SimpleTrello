from django import forms


class PasswordForm(forms.Form):
    form_password = forms.CharField()


class MailForm(forms.Form):
    mail_form = forms.EmailField()
