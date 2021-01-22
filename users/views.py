from django.shortcuts import render
from users.forms import CustomUserCreationForm


def register(request):
    form = CustomUserCreationForm()

    return render(request, 'register/register_user.html', {'form', form})
