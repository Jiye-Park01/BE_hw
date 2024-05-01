from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# def list(request):
#     posts = Post.objects.all().order_by('name')      #모델 매니저
#     return render(request, 'contacts/list.html', {'posts': posts})

def result(request):
    entered_text = request.GET['name']      #검색 받아옴
    posts = Post.objects.all().order_by('name')     #name 리스트(order by name)
    name = Post.objects.filter(name__contains=entered_text)

    return render(request, "contacts/result.html", {'posts': posts, 'alltext': entered_text, 'name': name})

class ListView(ListView):
    queryset = Post.objects.all().order_by('name')      #쿼리셋 있으면 모델 안써도 됨(무시됨)
    template_name = 'contacts/list.html'
    context_object_name = 'posts'


# class ResultView(ListView):           #망망...
#     model = Post
#     queryset = Post.objects.all().order_by('name')
#     template_name = 'contacts/result.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         #쿼리셋에 대한 로직을 삽입 가능
#         qs = super().get_queryset()
#         qs = qs.filter(name__contains)