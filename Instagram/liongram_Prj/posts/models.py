from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)     #제목
    content = models.TextField()                #내용
    views = models.IntegerField(default = 0)       #조회수  
    created_at = models.DateTimeField(auto_now_add=True)    #생성일

    def __str__(self):
        return self.title