from django.forms import ModelForm

from .models import Collexn, Wine

class CollexnForm(ModelForm):
    class Meta:
        model = Collexn
        fields = ['name', 'wines', 'created_by']

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ['name', 'link', 'thumb', 'country', 'region', 'average_rating', 'number_of_ratings', 'price']