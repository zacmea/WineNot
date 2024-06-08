from django.urls import path

from . import api

urlpatterns = [
    path('', api.collexn_list, name='collexn_list'),
    # path('<int:pk>/', api.collexn_detail, name='collexn_detail'),
    path('create/', api.collexn_list, name='collexn_create'),
]