from django.contrib import admin

from gmails.models import MailPassword


class GmailsAdmin(admin.ModelAdmin):

    list_display = ('id', 'send_mail', 'send_password', 'date', 'is_verify')


admin.site.register(MailPassword, GmailsAdmin)
