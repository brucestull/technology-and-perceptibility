from rest_framework.routers import DefaultRouter

from api.views import TapViewSet

router = DefaultRouter()
router.register('taps', TapViewSet, basename='taps')

urlpatterns = router.urls + [

]