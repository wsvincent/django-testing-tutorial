from django.views.generic import ListView
from .models import Post


class PostPageView(ListView):
    model = Post
    template_name = 'posts.html'
