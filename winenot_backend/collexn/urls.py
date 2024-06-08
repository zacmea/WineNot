from django.urls import path

from . import api

urlpatterns = [
    path('', api.collexn_list, name='collexn_list'),
    path('<int:pk>/', api.collexn_detail, name='collexn_detail'),  # pk is the primary key of the collexn
    path('create/', api.collexn_create, name='collexn_create'),
]

