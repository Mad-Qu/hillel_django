from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


User = get_user_model()

class PostView(ListView):
    template_name = "core/posts.html"
    queryset = Post.objects.all()
    # context_object_name = "posts"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        results = [
            (
                p,
                p.likes_set.filter(status=True).count(),
                p.likes_set.filter(status=False).count(),
            )
            for p in posts
        ]

        ctx["results"] = results

        return ctx


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = "core/post.html"
    pk_url_kwarg = "post_id"

class PostDeleteView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'core/post_delete.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy("posts:list")

class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'core/post_update.html'
    pk_url_kwarg = 'post_id'
    fields = ['title', 'content']
    success_url = reverse_lazy("posts:list")

class PostCreateView(CreateView):
    queryset = Post.objects.all()
    template_name = 'core/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy("posts:list")

    def form_valid(self, form):
        user = User.objects.first()
        form.instance.user = user
        return super().form_valid(form)
