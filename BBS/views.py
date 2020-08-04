from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def post_list(request):
    posts = Post.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'post_list.html', context)


def post_detail(request, p_num):
    now_post = get_object_or_404(Post, pk=p_num)
    if request.method == 'GET':
        now_post.views += 1
        now_post.save()
    comments = now_post.comment_set.all()
    context = {'post': now_post, 'comments': comments}
    return render(request, 'post_detail.html', context)

# Create your views here.


def comment_write(request, p_num):
    new_comment = Comment(
        post=get_object_or_404(Post, pk=p_num),
        author=request.POST.get('a'),
        contents=request.POST.get('c'),
    )
    new_comment.save()
    return redirect("/"+str(p_num))


def post_write(request):
    newPost = Post(
        title=request.POST.get('title'),
        author=request.POST.get('author'),
        contents=request.POST.get('content')
    )
    newPost.save()
    return redirect('/')


def post_form(request):
    return render(request, 'post_form.html')

def post_like(request, p_num):
    now_post = get_object_or_404(Post, pk=p_num)
    if request.POST['like'] == '좋아요':
        now_post.likes += 1
    else:
        now_post.dislikes += 1
    now_post.save()

    return redirect("/"+str(p_num))
