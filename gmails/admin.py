from django.contrib import admin

from gmails.models import SendPasswordMail


class GmailsAdmin(admin.ModelAdmin):

    list_display = ('id', 'send_mail', 'send_password', 'date', 'is_verify')


admin.site.register(SendPasswordMail, GmailsAdmin)
