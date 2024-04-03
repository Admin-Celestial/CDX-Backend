from django.urls import path
from .views import  User_History

urlpatterns = [
    path('user_history/<int:U_ID>/', User_History.as_view(), name='view-history'),
]
