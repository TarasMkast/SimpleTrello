from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as auth_login

from users.forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("aaaaaaaaaaaaaaaaaaaaaa")
            print(form)
            user = form.save()
            auth_login(request, user)
        return HttpResponse('Done!')
    form = CustomUserCreationForm()
    return render(request, 'register/register_user.html', {'form': form})
