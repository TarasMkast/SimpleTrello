from django.shortcuts import render, HttpResponse, redirect
from gmails.manager import ManagerAuthMail
from gmails.forms import PasswordForm, MailForm


def send_email_view(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        print(form)
        if form.is_valid():
            manage = ManagerAuthMail(form)
            manage.make_random_password()
            manage.send_email()
        return redirect('verify')
    form = MailForm()
    return render(request, 'authMail/authMail.html', {'form_mail': form})


def confirmation_view(request):

    return HttpResponse('Good')
