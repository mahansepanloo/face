from rest_framework import serializers
from .models import Post, Comment, Like, Follower


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'img', 'created', 'updated', 'totally_likes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'body', 'created']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'to_user', 'created']