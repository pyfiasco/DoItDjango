from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()   # 텍스트 형식 지정
    def __str__(self):
        return self.text[:200]