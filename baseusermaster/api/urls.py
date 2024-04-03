from django.urls import path
from . import views
from .views import MyTokenObtainPairView , signup, logout_view
#, LogTestAPI
from rest_framework_simplejwt.views import TokenRefreshView



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
#    path('log_test/', LogTestAPI.as_view(), name='log-test'),
]
