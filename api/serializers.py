from rest_framework import serializers

from taps.models import Tap

class TapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tap
        fields = ('id', 'title', 'url', 'url_label', 'description')