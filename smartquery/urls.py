from django.urls import path
from smartquery.views import generate_response
from .import views
from .views import LikedDisliked

urlpatterns = [
    path('Q&A/', views.generate_response, name='generate_response'),
    path('<int:pk>/ld/', LikedDisliked.as_view(), name='like-dislike')
]
