from rest_framework import serializers
from .models import Collexn, Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'

class CollexnSerializer(serializers.ModelSerializer):
    wines = WineSerializer(many=True, read_only=True)
    # by default, you'd normally only get back the id of the wine. This sends the id to the serializer and then will give you the full wine object
    class Meta:
        model = Collexn
        fields = '__all__'
