from django.shortcuts import render
from project.models import Project


def project_list(request):
    return render(request, 'project/project_list.html', {'projects': Project.objects.all()})

