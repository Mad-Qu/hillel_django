from .models import Post
from django.views.generic import ListView


class PostView(ListView):
    template_name = "core/posts.html"
    queryset = Post.objects.all()
    context_object_name = "posts"

