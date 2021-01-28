from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from rest_api.users_api.serializers import UserSerializer
from users.models import User


class UserViewSet(RetrieveAPIView, ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

