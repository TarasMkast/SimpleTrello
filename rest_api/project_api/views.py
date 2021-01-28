from rest_framework import viewsets
from project.models import Project
from rest_api.project_api.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
