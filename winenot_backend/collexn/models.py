import uuid 

from django.db import models
# from django.contrib.auth.models import User
from account.models import User
from django.contrib.auth import get_user_model

#Class for storing wine data, based on data that will be avail from Vivino API
class Wine(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    thumb = models.URLField()
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    number_of_ratings = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

#Class for storing collections of wines
class Collexn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    wines = models.ManyToManyField(Wine, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    