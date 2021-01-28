from rest_framework.routers import DefaultRouter
from rest_api.project_api.views import ProjectViewSet


router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
urlpatterns = router.urls
