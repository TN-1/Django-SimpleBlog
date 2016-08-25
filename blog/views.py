from django.shortcuts import render, get_object_or_404
from blog.models import Post, BlogInfo

# Create your views here.

def index(request):
    posts = Post.objects.filter(published=True)
    info = BlogInfo.objects.first()
    return render(request, 'blog/index.html',{'posts':posts , 'info':info})

def post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request, 'blog/post.html',{'post':post})
