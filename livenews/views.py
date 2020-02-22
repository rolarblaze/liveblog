from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    nxt ={
        'posts': Post.objects.all()
    }
    return render(request, 'livenews/home.html', nxt)

def about(request):
    return render(request, 'livenews/about.html')
