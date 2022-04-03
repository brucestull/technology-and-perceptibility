from rest_framework.routers import DefaultRouter

from api.views import TapViewSet, UserViewSet

router = DefaultRouter()
router.register('taps', TapViewSet, basename='taps')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [

]