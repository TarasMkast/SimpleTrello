from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       )
from users.models import CustomAbstractBaseUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomAbstractBaseUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomAbstractBaseUser
        fields = ('email',)
