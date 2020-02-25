from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    nxt ={
        'posts': Post.objects.all()
    }
    return render(request, 'livenews/home.html', nxt)

class NewsListView(ListView):
    model = Post
    template_name = 'livenews/home.html' #<app name>--<model name>---<viewtype>.html
    context_name = 'posts'

def about(request):
    return render(request, 'livenews/about.html')
