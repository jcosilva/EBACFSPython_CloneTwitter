from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('like/<int:id>/', views.like_tweet, name='like_tweet'),
    path('delete/<int:id>/', views.delete_tweet, name='delete_tweet'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    path('search/', views.search_users, name='search_users'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]