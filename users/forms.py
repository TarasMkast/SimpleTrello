from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       )
from users.models import CustomBaseUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomBaseUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomBaseUser
        fields = ('email',)
