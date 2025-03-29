from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('my-posts/', views.user_posts, name='user_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]