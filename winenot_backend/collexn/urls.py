#these are all prefixed with /collexns/

from django.urls import path

from . import api

urlpatterns = [
    path('', api.collexn_list, name='collexn_list'),
    path('create/', api.collexn_create, name='collexn_create'),
    path('<pk>/', api.collexn_detail, name='collexn_detail'),
    path('<pk>/delete/', api.collexn_delete, name='collexn_delete'),
    path('api/collexns/<pk>/remove_wine/<wine_id>/', remove_wine_from_collexn, name='remove_wine_from_collexn'),
]