from django.db import models
from config import settings


class TimestampMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampMixin):
    title = models.CharField(
        max_length=100, null=False, blank=False
    )  # blank=False - нельзя оставлять пустым
    content = models.TextField(null=False, blank=False)
    image = models.CharField(
        max_length=255, null=True, blank=True
    )  # blank=True - можно оставлять пустым
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return f"{self.title}"


class Likes(TimestampMixin):
    post = models.ForeignKey("Post", null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE
    )
    status = models.BooleanField(null=True, blank=True)
