from django.core.mail import send_mail as sm
from django.http import HttpResponse
from django.utils.crypto import get_random_string


class ManagerAuthMail:

    def __init__(self, address_mail):
        self.address_mail = address_mail
        self.input_password = None

    def make_random_password(self, length=10,
                             allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                           'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                           '23456789'):
        self.password = get_random_string(length, allowed_chars)
        return self.password

    def send_email(self, password):
        res = sm(
            subject='Підтвердження пошти',
            message='Код підтвердження пошти: ' + password,
            from_email='',
            recipient_list=[self.address_mail],
            fail_silently=False
        )

        return HttpResponse(res)

    def confirmation_email(self, input_password):
        self.input_password = input_password
        if input_password == self.password:
            return True
        return False
