from rest_framework import serializers
from .models import Collexn, Wine, CollexnWine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'

class CollexnWineSerializer(serializers.ModelSerializer):
    wine = WineSerializer()

    class Meta:
        model = CollexnWine
        fields = ['wine']

class CollexnSerializer(serializers.ModelSerializer):
    wines = CollexnWineSerializer(source='collexnwine_set', many=True, read_only=True)

    class Meta:
        model = Collexn
        fields = '__all__'
