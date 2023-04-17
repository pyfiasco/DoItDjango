"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (HomePageView,
                    AboutPageView,                    
                    BlogListView, 
                    BlogDetailView, 
                    BlogCreateView, 
                    BlogUpdateView, 
                    BlogDeleteView,
                    )

urlpatterns = [    
    path('', HomePageView.as_view(), name='home'),    # class view 연결
    path('about/', AboutPageView.as_view(), name='about'),    # class view 연결
    path('blog/', BlogListView.as_view(), name='blog'),    # class view 연결
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blog/new/', BlogCreateView.as_view(), name='post_new'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),  
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),


]



