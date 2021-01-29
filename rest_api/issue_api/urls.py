from rest_framework.routers import DefaultRouter
from rest_api.issue_api.views import IssueViewSet


router = DefaultRouter()
router.register('issue', IssueViewSet, basename='issue')
urlpatterns = router.urls
