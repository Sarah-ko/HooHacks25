from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Like

def home_view(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts' : posts})

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
    
    return render(request, 'user_posts.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    # Check if the user has already liked the post
    existing_like = Like.objects.filter(user=request.user, post=post).first()
    
    if existing_like:
        # already liked the post, remove the like
        existing_like.delete()
    else:
        #hasn't liked the post yet, create a like
        Like.objects.create(user=request.user, post=post)
    
    return redirect('home')