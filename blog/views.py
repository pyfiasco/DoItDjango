from django.views.generic import ListView, DetailView # new
from .models import Post
# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = "blog.html"


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = 'post_detail.html'