from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50) #이름
    phone_num = models.CharField(max_length=12) #전화번호
    email = models.EmailField()  #이메일
    created_at = models.DateField(auto_now_add=True)    #연락처 생성 시간

    def __str__(self):
        return self.name