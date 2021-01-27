from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from gmails.forms import PasswordForm
from gmails.manager import ManagerAuthMail
from gmails.models import MailPassword
from users.forms import CustomUserCreationForm
from users.models import User


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = user.email
            db_send_password_mail = MailPassword(send_mail=email)
            manage = ManagerAuthMail(email)
            send_password = manage.make_random_password()
            manage.send_email(send_password)
            db_send_password_mail.send_password = send_password
            db_send_password_mail.save()
            return redirect('users:verify')
    form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def verify_mail(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            input_password = form.cleaned_data.get('form_password')
            try:
                mail_verify = MailPassword.objects.get(send_password=input_password)
                user = User.objects.get(email=mail_verify.send_mail)
                mail_verify.is_verify = True
                user.is_active = True
                user.save()
                mail_verify.save()

            except:
                raise Http404("Дані відсутні, поверніть назад на головну сторінку ")
            return HttpResponse('Ви підтвердили пошту!')
    form = PasswordForm()
    return render(request, 'registration/verify.html', {'form_verify': form})
