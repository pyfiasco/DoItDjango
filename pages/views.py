from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


'''
def homePageView(request):                # 함수 view 정의
    return HttpResponse('Hello, World!')
'''

class HomePageView(TemplateView):         # class view 정의
    template_name = 'home.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'