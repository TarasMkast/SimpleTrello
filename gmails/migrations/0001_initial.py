# Generated by Django 3.1.5 on 2021-01-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_mail', models.EmailField(blank=True, max_length=254, verbose_name='Електронна пошта')),
                ('send_password', models.CharField(blank=True, max_length=10, verbose_name='Відправлений пароль')),
                ('input_password', models.CharField(default='-', max_length=10, verbose_name='Отриманий пароль')),
                ('is_verify', models.BooleanField(default=False, verbose_name='Статус підтвердження')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата операції')),
            ],
            options={
                'verbose_name': 'Підтвердження пошти',
                'verbose_name_plural': 'Підтвердження пошти',
            },
        ),
    ]
