from django.http import HttpResponse
from .models import Post


def posts(request):
    posts = Post.objects.all()
    results = ", ".join([post.title for post in posts])
    return HttpResponse(results)
