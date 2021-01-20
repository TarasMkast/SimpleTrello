from django.urls import path
from gmails import views
urlpatterns = [
    path('', views.send_email, name='send_email'),
]
