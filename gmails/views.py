# from datetime import timedelta
# from django.shortcuts import (render,
#                               HttpResponse,
#                               redirect,
#                               )
# from django.utils import timezone
#
# from gmails.manager import ManagerAuthMail
# from gmails.forms import (PasswordForm,
#                           MailForm,
#                           )
# from gmails.models import MailPassword
#
#
# def send_email_view(request):
#     if request.method == "POST":
#         form = MailForm(request.POST)
#         if form.is_valid():
#             message = form.cleaned_data.get('mail_form')
#             manage = ManagerAuthMail(message)
#             send_password = manage.make_random_password()
#             manage.send_email(send_password)
#             db_send_password_mail = MailPassword(send_mail=message, send_password=send_password)
#             db_send_password_mail.save()
#         return redirect('verify')
#     form = MailForm()
#     return render(request, 'authMail/authMail.html', {'form_mail': form})
#
#
# def confirmation_view(request):
#     db_send_password_mail = MailPassword.objects.values_list('send_password')
#     if request.method == 'POST':
#         form = PasswordForm(request.POST)
#         if form.is_valid():
#             input_password = form.cleaned_data.get('form_password')
#             for db in db_send_password_mail:
#                 if input_password == db[0]:
#                     db_send_password_m = MailPassword.objects.get(send_password=db[0])
#                     now = timezone.now() - timedelta(minutes=60)
#                     if db_send_password_m.date > now:
#                         db_send_password_m.input_password = db[0]
#                         db_send_password_m.is_verify = True
#                         db_send_password_m.save()
#                         return HttpResponse('Вітаємо, ви підтвердили вашу пошту!')
#                     return HttpResponse('Час активація вийшов! Пошта не активована, спробуйте знову.')
#             return HttpResponse('Код не вірний!')
#     form = PasswordForm()
#     return render(request, 'authMail/verifyMail.html', {'form_verify': form})
