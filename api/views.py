from rest_framework import viewsets

from taps.models import Tap
from api.serializers import TapSerializer

class TapViewSet(viewsets.ModelViewSet):
    queryset = Tap.objects.all()
    serializer_class = TapSerializer


