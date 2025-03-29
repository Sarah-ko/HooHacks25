from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('my-posts/', views.user_posts, name='user_posts'),
]