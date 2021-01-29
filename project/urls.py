from django.urls import path
from project import views

app_name = 'project'

urlpatterns = [
    path('projects/', views.project_list, name='project_list')
]
