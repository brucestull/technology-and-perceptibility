from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import TapViewSet, UserViewSet, CurrentUserView
# from . import views

app_name = 'api'
router = DefaultRouter()
router.register('taps', TapViewSet, basename='taps')
# router.register('taps', views.TapViewSet, basename='taps')
router.register('users', UserViewSet, basename='users')
# router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view()),
    # path('currentuser/', views.CurrentUserView.as_view()),
]