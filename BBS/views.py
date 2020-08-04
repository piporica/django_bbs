from django.shortcuts import render, get_object_or_404
from .models import *


def post_list(request):
    posts = Post.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'post_list.html', context)


def post_detail(request, p_num):
    now_post = get_object_or_404(Post, pk=p_num)
    comments = now_post.comment_set.all()
    context = {'post': now_post, 'comments': comments}
    return render(request, 'post_detail.html', context)
# Create your views here.
