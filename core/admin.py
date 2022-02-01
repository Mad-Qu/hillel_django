from django.contrib import admin
from core import models

# from .models import Likes, Post

# @admin.register(Likes)
# class LikeAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass


class TabularInlineLikes(admin.TabularInline):
    model = models.Likes


class PostAdmin(admin.ModelAdmin):
    inlines = [TabularInlineLikes]
    list_display = ("title", "user", "created_at")


admin.site.register(models.Post, PostAdmin)
