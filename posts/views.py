from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

def home_view(request):
    return render(request, 'home.html')

# Create your views here.
@login_required
def create_post(request):
    print("debug statement\n")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})
@login_required
def user_posts(request):
    # Get all posts created by the logged-in user
    posts = Post.objects.filter(author=request.user)
    
    return render(request, 'posts/user_posts.html', {'posts': posts})