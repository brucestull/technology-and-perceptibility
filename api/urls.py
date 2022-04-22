from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import TapViewSet, UserViewSet, CurrentUserView, PublicViewSet
# from . import views

app_name = 'api'
router = DefaultRouter()
router.register('taps', TapViewSet, basename='taps')
router.register('users', UserViewSet, basename='users')
router.register('public', PublicViewSet, basename='public')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view()),
]