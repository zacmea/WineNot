
#Trying to enable the ability to remove a wine from a collection, here to line 25
# from rest_framework import serializers
# from .models import Collexn, Wine, 
# #                               CollexnWine

# class WineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wine
#         fields = '__all__'

# # class CollexnWineSerializer(serializers.ModelSerializer):
# #     wine = WineSerializer()

# #     class Meta:
# #         model = CollexnWine
# #         fields = ['wine']

# class CollexnSerializer(serializers.ModelSerializer):
#     wines = CollexnWineSerializer(source='collexnwine_set', many=True, read_only=True)

#     class Meta:
#         model = Collexn
#         fields = '__all__'


# What was working before I started trying to allow for the removal of a wine from a collection :
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