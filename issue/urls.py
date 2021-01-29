from django.urls import path
from issue import views

app_name = 'issue'

urlpatterns = [
    path('project/<int:pk>', views.catalog_issue, name='project'),
    path('changeStatus/', views.change_status_issue, name='change_status')
]
