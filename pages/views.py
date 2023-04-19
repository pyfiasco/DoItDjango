from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import (CreateView,
                                       DeleteView,
                                       UpdateView,
                                       )
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def homePageView(request):
    return HttpResponse('page home')


class HomePageView(TemplateView):
    model = Post
    template_name = 'home.html'
    

class AboutPageView(TemplateView):  
    template_name = 'about.html'


class BlogListView(ListView):
    model = Post 
    template_name = 'post_list.html'
    context_object_name = 'all_posts_list'  # list로 사용할 이름 지정


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post 
    template_name = 'post_new.html' 
    fields = ['title', 'author', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("post_list")


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']




