from rest_framework import generics, permissions
from .models import Post, Comment, Like, Follower
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, FollowSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user

            followed_users = Follower.objects.filter(from_user=user).values_list('to_user', flat=True)

            return Post.objects.filter(user__in=followed_users)
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowListCreateView(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)


class FollowDetailView(generics.RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]