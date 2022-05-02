from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from taps.models import Tap
from api.serializers import TapSerializer, UserSerializer, UserUpdateSerializer


# We use this view for getting the 'public' link set.
class PublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tap.objects.filter(public=True)
    serializer_class = TapSerializer


# We use this view for getting User info and their TAPs.
class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
    permission_classes = [IsAuthenticated]


# We use this view for updating user profile.
class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    def get_object(self):
        return self.request.user
    permission_classes = [IsAuthenticated]


# We can use this view to get a User's TAPs. This is not implemented in front end.
class TapViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Tap.objects.filter(author=self.request.user.id)
    serializer_class = TapSerializer
    # This permission requires user to be authenticated in order to add new TAP.
    permission_classes = [IsAuthenticated]


