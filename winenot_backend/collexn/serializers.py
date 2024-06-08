from rest_framework import serializers
from .models import Collexn, Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'

class CollexnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collexn
        fields = '__all__'
