from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required

def list(request):
    #존재하는 모든 카테고리 확인할 수 있도록
    categories = Category.objects.all()

    #선택한 카테고리 id
    category_id = request.GET.get('category')

    #카테고리 필터링
    if category_id:
        category = get_object_or_404(Category, id = category_id)
        posts = category.posts.all().order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/list.html', {'posts': posts, 'categories':categories})
    

#CRUD
@login_required
def create(request):
    #존재하는 모든 카테고리 확인할 수 있도록
    categories = Category.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get('content')
        video = request.FILES.get('video')
        image = request.FILES.get('image')


        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user, 
            image = image,
            video = video
        )

        #다대다 카테고리 연결
        for category in category_list:
            post.category.add(category)

        return redirect('blog:list')
    return render(request, 'blog/create.html', {'categories': categories})

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'blog/detail.html', {'post':post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        if video:
            post.video.delete()
            post.video = video
        if image:
            post.image.delete()
            post.image = image

        post.save()
        return redirect('blog:detail', id)
    return render(request, 'blog/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('blog:list')



def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post
        )
        return redirect('blog:detail', post_id)
    

def add_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.add(request.user)
    return redirect('blog:detail', post_id)

def remove_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.remove(request.user)
    return redirect('blog:detail', post_id)


def mylike(request):
    liked_posts = Post.objects.filter(like=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts':liked_posts})