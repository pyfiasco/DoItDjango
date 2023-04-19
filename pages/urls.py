"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import (HomePageView, 
                    homePageView, 
                    AboutPageView, 
                    BlogDetailView,
                    BlogCreateView,
                    BlogDeleteView,
                    BlogUpdateView,
                    BlogListView,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pages/', homePageView, name='home_pages'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  
    path('blog/new/', BlogCreateView.as_view(), name='post_new'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('blog/',BlogListView.as_view(), name='post_list'),

    
]
