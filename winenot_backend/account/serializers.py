#NOTE: This file is used to serialize the data, which converts it into a format that can be easily rendered into JSON

from .models import  User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')