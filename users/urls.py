from django.urls import path
from django.contrib.auth import views
from users import views as users_views
from users.views import RegisterFormView

urlpatterns = [
    #path('', users_views.register, name='registration'),
    path('register/', RegisterFormView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name='login'),

]
