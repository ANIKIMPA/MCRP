from rest_framework import routers
from .viewsets import ItemViewSet

router = routers.SimpleRouter()
router.register("items", ItemViewSet)

urlpatterns = router.urls