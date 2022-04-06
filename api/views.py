from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth import get_user_model

from taps.models import Tap
from api.serializers import TapSerializer, UserSerializer
from api.permissions import IsAuthorOrReadOnly

class TapViewSet(viewsets.ModelViewSet):
    queryset = Tap.objects.all()
    serializer_class = TapSerializer
    permission_classes = [IsAuthorOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
