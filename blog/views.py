from django.shortcuts import render, get_object_or_404
from blog.models import Post, BlogInfo, Comment
from .forms import CommentForm
# Create your views here.

def index(request):
    posts = Post.objects.filter(published=True)
    info = BlogInfo.objects.first()
    return render(request, 'blog/index.html',{'posts':posts , 'info':info})

def post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    comments = Comment.objects.filter(slug=slug)
    info = BlogInfo.objects.first()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.POST.get('username','')
            comment.content = request.POST.get('content','')
            comment.slug = slug
            comment.save()
            return render(request, 'blog/post.html', {'post': post, 'comments': comments, 'form': form, 'info':info})
    else:
        form = CommentForm()
    if not comments:
        return render(request, 'blog/post.html',{'post':post, 'form':form, 'info':info})
    elif comments:
        return render(request, 'blog/post.html',{'post':post, 'comments':comments, 'form':form, 'info':info})
