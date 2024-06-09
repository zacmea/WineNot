from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from . import api

urlpatterns = [
    path('signup/', api.signup, name='signup'),
    # path('logout/', api.logout_view, name='logout'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', api.me, name='me'),
]
