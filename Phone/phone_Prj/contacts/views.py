from django.shortcuts import render
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('name')      #모델 매니저
    return render(request, 'contacts/list.html', {'posts': posts})

def result(request):
    entered_text = request.GET['name']      #검색 받아옴
    posts = Post.objects.all().order_by('name')     #name 리스트(order by name)
    name = Post.objects.filter(name__contains=entered_text)

    return render(request, "contacts/result.html", {'posts': posts, 'alltext': entered_text, 'name': name})