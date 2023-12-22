from .views import PostList, GenericPostApiView
from django.urls import path

urlpatterns = [
    path('posts/', GenericPostApiView.as_view()),
]
