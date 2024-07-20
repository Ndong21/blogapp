
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm, CreateUserForm, LoginForm, PostForm

# authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homepage(request):
    return render(request, 'webapp/homepage.html',)

def register(request):

    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('login')
    
    context = {
        'registerform': form
    }

    return render(request, 'webapp/register.html', context)

def login(request):
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return HttpResponseRedirect('blog')
        
    context = {
        'loginform':form
    }


    return render(request, 'webapp/login.html', context)

def user_logout(request):

    auth.logout(request)

    return HttpResponseRedirect("")



def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
            )
            post.save()
            return HttpResponseRedirect(request.path_info)
   
    context = {
        'posts': posts,
        'post':PostForm

    }
    return render(request, 'webapp/index.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments, 
        'form': CommentForm(),
    }

    return render(request, 'webapp/detail.html', context)