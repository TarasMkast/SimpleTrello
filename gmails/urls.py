from django.urls import path
from gmails import views
urlpatterns = [
    path('', views.send_email_view, name='send_email'),
    path('verify/', views.confirmation_view, name='verify')
]
