from django.contrib import admin
from .models import *

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    pass
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('totally_likes',)