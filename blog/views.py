from django.views.generic import ListView, DetailView 
# new/update/delete blog생성 위해
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = "blog.html"


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = 'post_detail.html'
    

class BlogCreateView(CreateView):  # new blog 생성 view
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):  # update view
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):  
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home_blog')  # URL 리디렉션을 실행하지 않도록
