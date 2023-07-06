from rest_framework import serializers
from users.models import User
from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

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
        
    