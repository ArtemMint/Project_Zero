from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Blog, Comment
from .forms import BlogForm, CommentForm


def home_view(request):
    return render(
        request, 
        'blog/home.html',
        {})


def blog_view(request):
    blog_list = Blog.objects.order_by('-published_date')
    return render(
        request, 
        'blog/blog.html',
        {'blog_list' : blog_list})


def blog_detail_view(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except blog.DoesNotExist:
        raise Http404("Blog does not exist")

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():         
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.published_comment = timezone.now()
            new_comment.blog = blog
            new_comment.save()
    else:
        comment_form = CommentForm()                   
    return render(
        request,
        'blog/blog_detail.html',
        {'blog': blog,
        'comment_form': comment_form})

def new_post_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('/blog/', pk=blog.pk)
    else:
        form = BlogForm()
    return render(
    request, 
    'blog/new_post.html',
    {'form' : form}) 