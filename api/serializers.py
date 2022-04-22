from rest_framework import serializers
from django.contrib.auth import get_user_model

from taps.models import Tap

class NestedTapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tap
        fields = (
                'id',
                'url',
                'url_label',
                'description',
                'public',
                )

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = get_user_model()
        fields = ('id', 'username')

class TapSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Tap
        fields = ('id', 'author', 'author_detail', 'url', 'url_label', 'description', 'public')

class UserSerializer(serializers.ModelSerializer):
    taps_detail = NestedTapSerializer(many=True, read_only=True, source='taps')
    class Meta: 
        model = get_user_model()
        fields = ('id', 'username', 'taps_detail')