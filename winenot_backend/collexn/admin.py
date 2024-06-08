from django.contrib import admin

# Register your models here.
from .models import Wine, Collexn

admin.site.register(Wine)
admin.site.register(Collexn)