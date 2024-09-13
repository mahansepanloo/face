from rest_framework import serializers
from .models import Post, Comment, Like, Follower


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'img', 'created', 'updated', 'totally_likes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'body', 'created']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'from_user', 'to_user', 'created']