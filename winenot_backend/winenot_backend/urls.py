# NOTE: This file is the root URL configuration for winenot_backend project, as defined in settings.py.


from django.contrib import admin
from django.urls import path, include, resolve


urlpatterns = [
    path('api/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('api/collexns/', include('collexn.urls')),
]
 

def print_url_patterns(urlpatterns, parent=''):
    for url_pattern in urlpatterns:
        if hasattr(url_pattern, 'url_patterns'):
            print_url_patterns(url_pattern.url_patterns, parent + str(url_pattern.pattern))
        else:
            print(f'Pattern: {parent}{url_pattern.pattern}, Name: {url_pattern.name}, View: {url_pattern.callback}')

print_url_patterns(urlpatterns)