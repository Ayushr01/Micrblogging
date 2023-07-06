from rest_framework import serializers
from .models import Post
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    """
    serializes POst data
    """

    class Meta:
        model = Post
        fields = '__all__'