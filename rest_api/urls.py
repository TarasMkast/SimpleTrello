from django.urls import path, include

urlpatterns = [
    path('issue/', include('rest_api.issue_api.urls')),
    path('project/', include('rest_api.project_api.urls')),
    path('user/', include('rest_api.users_api.urls')),
]
