from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('blog', views.blog_index, name='blog'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'), 

]    