from django.contrib import admin

# Register your models here.
from .models import Wine, Collexn, User

admin.site.register(Wine)
admin.site.register(Collexn)
admin.site.register(User)