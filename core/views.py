from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def create_post(request):
    return render(request, 'create_post.html')

def my_posts(request):
    return render(request, 'my_posts.html')

def login_view(request):
    return render(request, 'login.html')
