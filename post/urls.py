from django.urls import path  
from .views import (  
    PostListCreateView,  
    PostDetailView,  
    CommentListCreateView,  
    CommentDetailView,  
    LikeListCreateView,  
    FollowListCreateView,  
    FollowDetailView,  
)  

urlpatterns = [  
    path('posts', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('comments', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
    path('likes', LikeListCreateView.as_view(), name='like-list-create'),
    path('follows', FollowListCreateView.as_view(), name='follow-list-create'),
    path('follows/<int:pk>', FollowDetailView.as_view(), name='follow-detail'),
]