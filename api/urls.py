from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'
router = DefaultRouter()
router.register('taps', views.TapViewSet, basename='taps')
router.register('public', views.PublicViewSet, basename='public')


urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUserView.as_view()),
    path('user-update/', views.UserUpdateView.as_view()),
]