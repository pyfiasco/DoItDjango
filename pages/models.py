from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=200) 
    '''
    author = models.ForeignKey(
        'accounts.CustomUser', on_delete=models.CASCADE,
    )     
    '''
    author = models.ForeignKey( get_user_model(), on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True)    
    body = models.TextField()

    def __str__(self):
        return self.title[:50]
    
    # 표준 url 설정
    def get_absolute_url(self):
        # url alias으로 객체 참조하기위한 함수         
        return reverse("post_detail", kwargs={"pk": self.pk})
        # self.pk= str(self.id)
  