from rest_framework import routers
from .viewsets import FileViewSet, ItemViewSet

router = routers.SimpleRouter()
router.register("files", FileViewSet)
router.register("items", ItemViewSet)

urlpatterns = router.urls