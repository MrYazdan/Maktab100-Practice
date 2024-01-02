from .views import (PostList,
                    GenericPostListCreateApiView,
                    GenericCommentListCreateApiView,
                    GenericCommentDetailApiView, GenericPostDetailApiView)
from django.urls import path

urlpatterns = [

    path('posts/', GenericPostListCreateApiView.as_view()),
    path('posts/<pk>', GenericPostDetailApiView.as_view(), name="post-detail"),
    # Comments
    path('comments/', GenericCommentListCreateApiView.as_view()),
    path('comments/<pk>', GenericCommentDetailApiView.as_view(), name="comment-detail"),
]
