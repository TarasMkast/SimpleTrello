from rest_framework import viewsets
from issue.models import Issue
from rest_api.issue_api.serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
