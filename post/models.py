from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='post_images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def totally_likes(self):
        return self.plike.count()

    def __str__(self):
        return f'Post by {self.user.username} on {self.created} '


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomments')
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.id}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ulike')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='plike')

    def __str__(self):
        return f'Like by {self.user.username} on post {self.post.id}'


class Follower(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user.username} following {self.to_user.username}'