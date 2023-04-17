from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogListView(ListView):               # object_list 반환
    model = Post                            # model 지정
    template_name = 'post_list.html'             # templat file 지정
    context_object_name = 'all_posts_list'  # objec_list -> all_posts_list


class BlogDetailView(DetailView):  
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):            # form 생성
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):   # form update
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):  
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog')
