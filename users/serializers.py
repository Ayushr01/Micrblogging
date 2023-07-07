from rest_framework import serializers
from posts.models import Post
from users.models import User
from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
import datetime

class UserRegistraionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
    
    def validate_password(self, obj):
        """
        Validates if password is in required Format or not
        """
        if(len(obj) < 8):
            raise ValidationError("Password must be atleast 8 characters Long")
        elif(obj.islower()):
            raise ValidationError("Atleast 1 Caps Letter is required")
        
        return obj


class UserSerializer(ModelSerializer):
     """
     serializes user data
     """
     class Meta:
        model = User
        fields = '__all__'
        
    
class UserTimeLineSerializer(ModelSerializer):
    """
    serializes posts data for users timeline
    """
    creator = serializers.SerializerMethodField()
    post_date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('content', 'creator', 'post_date')

    def get_creator(self, obj):
        """
        returns creator name
        """
        return obj.created_by.user_name
    
    def get_post_date(self, obj):
        """
        converts server datetime into DD MM YY HH MM SS format.
        """
        return obj.post_date.strftime('%d-%m-%Y %H:%M:%S')