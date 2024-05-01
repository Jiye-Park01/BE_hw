from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/list.html', {'posts': posts})

def result(request):
    entered_text = request.GET['search']
    posts = Post.objects.filter( Q(title__contains=entered_text) | Q(content__contains=entered_text)).order_by('-created_at')
    

    return render(request, 'posts/result.html', {'entered_text': entered_text, 'posts':posts})

#CRUD
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title = title,
            content = content, 
        )
        return redirect('list')
    return render(request, 'posts/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    post.views = post.views + 1
    post.save()
    return render(request, 'posts/detail.html', {'post':post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('detail', id)
    return render(request, 'posts/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('list')