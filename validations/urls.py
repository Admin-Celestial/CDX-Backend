from django.urls import path
from .views import validator_v, view_val, ApproveDisapprove

urlpatterns = [
    path('validator/', validator_v.as_view(), name='validator'),
    path('dislikes/',view_val, name='dislikes'),
    path('<int:pk>/ad/', ApproveDisapprove.as_view(), name='approve-disapprove')
]
