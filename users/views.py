from django.http import HttpResponse
from django.shortcuts import render

from users.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = "/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        print(form)
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaa")
#             print(form)
#             user = form.save()
#             auth_login(request, user)
#             return HttpResponse('Done!')
#     form = CustomUserCreationForm()
#     return render(request, 'registration/base.html', {'form': form})
