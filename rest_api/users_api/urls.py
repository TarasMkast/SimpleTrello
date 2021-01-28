from rest_framework.routers import DefaultRouter
from rest_api.users_api.views import UserViewSet


router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns = router.urls
