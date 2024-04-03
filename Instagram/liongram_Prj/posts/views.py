from django.shortcuts import render
from .models import Post
from django.db.models import Q

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/list.html', {'posts': posts})

def result(request):
    entered_text = request.GET['search']
    posts = Post.objects.filter( Q(title__contains=entered_text) | Q(content__contains=entered_text)).order_by('-created_at')
    

    return render(request, 'posts/result.html', {'entered_text': entered_text, 'posts':posts})