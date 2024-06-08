# NOTE: This file is the root URL configuration for winenot_backend project, as defined in settings.py.


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('api/collexns/', include('collexn.urls')),
]
 