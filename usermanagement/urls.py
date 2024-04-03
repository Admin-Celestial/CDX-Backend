from django.urls import path
from .views import TempUserMasterView


urlpatterns = [
    path('temp-users/', TempUserMasterView.as_view(), name='temp-user-list'),
    path('temp-users/<int:id>/', TempUserMasterView.as_view(), name='temp-user-detail'),
    path('temp-users/create/', TempUserMasterView.as_view(), name='temp-user-create'),
    path('temp-users/<int:id>/update/', TempUserMasterView.as_view(), name='temp-user-update'),
    path('temp-users/<int:id>/delete/', TempUserMasterView.as_view(), name='temp-user-delete'),
]
