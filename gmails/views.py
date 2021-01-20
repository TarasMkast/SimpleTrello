from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm


def send_email(request):
    res = sm(
        subject='Підтвердження пошти',
        message='Код підтвердження пошти: ',
        from_email='',
        recipient_list=['taras.m@yleaf.co'],
        fail_silently=False
    )
    #return HttpResponse('Email sent: ' + str(res))
