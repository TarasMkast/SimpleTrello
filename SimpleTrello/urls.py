from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_api.urls')),
    path('', include('users.urls')),
    path('', include('project.urls')),
    path('', include('issue.urls')),
]
