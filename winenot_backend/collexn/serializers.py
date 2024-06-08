#NOTE: This file is used to serialize the data, which converts it into a format that can be easily rendered into JSON

from .models import Collexn, Wine
from rest_framework import serializers

Class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'

Class CollexnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collexn
        fields = '__all__'