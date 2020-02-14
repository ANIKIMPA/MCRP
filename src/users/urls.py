from rest_framework import routers
from .views import LoginLevelViewSet

router = routers.DefaultRouter()
router.register("loginLevels", LoginLevelViewSet)

urlpatterns = router.urls