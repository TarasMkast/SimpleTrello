from django.shortcuts import (render,
                              HttpResponse,
                              redirect,
                              )
from gmails.manager import ManagerAuthMail
from gmails.forms import (PasswordForm,
                          MailForm,
                          )
from gmails.models import SendPasswordMail
from users.models import CustomAbstractBaseUser

mass = []


def send_email_view(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get('mail_form')
            manage = ManagerAuthMail(message)
            send_password = manage.make_random_password()
            manage.send_email(send_password)
            db_send_password_mail = SendPasswordMail(send_mail=message, send_password=send_password)
            db_send_password_mail.save()
            print(send_password)
            mass.append(db_send_password_mail)
        return redirect('verify')
    form = MailForm()
    return render(request, 'authMail/authMail.html', {'form_mail': form})


def confirmation_view(request):
    db_send_password_mail = mass[0]
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            input_password = form.cleaned_data.get('form_password')
            if input_password == db_send_password_mail.send_password:
                db_send_password_mail.input_password = input_password
                db_send_password_mail.is_verify = True
                db_send_password_mail.save()
                mass.clear()
                return HttpResponse('Вітаємо, ви підтвердили вашу пошту!')
            return HttpResponse('Код не вірний!')
    form = PasswordForm()
    return render(request, 'authMail/verifyMail.html', {'form_verify': form})
