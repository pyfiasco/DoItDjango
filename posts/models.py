from django.db import models
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(              # field type 정의  - 객체로서
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):                        # str method 정의  - text 표시
        return self.title

    def get_absolute_url(self):  
        return reverse('post_detail', args=[str(self.id)])  # url template name을 이용한 객체 참조
