from django.db import models


class MailPassword(models.Model):

    send_mail = models.EmailField(blank=True, verbose_name='Електронна пошта')
    send_password = models.CharField(max_length=10, blank=True, verbose_name='Відправлений пароль')
    input_password = models.CharField(max_length=10, default='-', verbose_name='Отриманий пароль')
    is_verify = models.BooleanField(default=False, verbose_name='Статус підтвердження')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата операції')

    class Meta:
        verbose_name = 'Підтвердження пошти'
        verbose_name_plural = 'Підтвердження пошти'

    def __repr__(self):
        return self.id
