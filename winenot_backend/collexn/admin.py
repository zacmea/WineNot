from django.contrib import admin

# Register your models here.
from .models import Wine, Collexn, CollexnWine

admin.site.register(Wine)
admin.site.register(Collexn)
admin.site.register(CollexnWine)