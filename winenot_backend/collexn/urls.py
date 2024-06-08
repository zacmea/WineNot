#these are all prefixed with /collexns/

from django.urls import path

from . import api

urlpatterns = [
    path('', api.collexn_list, name='collexn_list'),
    path('create/', api.collexn_create, name='collexn_create'),
    path('<pk>/', api.collexn_detail, name='collexn_detail'),
]