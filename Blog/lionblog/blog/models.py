from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return f'[{self.name}]'
    
class Post(models.Model):
    title = models.CharField(max_length=50)     # 글의 제목, 최대 길이는 50
    content = models.TextField()        # 글의 본문
    created_at=models.DateTimeField(auto_now_add = True)        # 생성 일자
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "posts")
    category = models.ManyToManyField(to = Category, through = "PostCategory", related_name = "posts")
    like = models.ManyToManyField(to = User, through = "Like", related_name = "liked_posts")

    def __str__(self):
        return f'[{self.id}] {self.title}'
    
class Like(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name="user_likes")
    
class PostCategory(models.Model):       #중간테이블 생성
    category = models.ForeignKey(to = Category, on_delete = models.PROTECT, related_name = "categories_postcategory")
    post = models.ForeignKey(to = Post, on_delete= models.CASCADE, related_name = "posts_postcategory")

class Comment(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name = "comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'