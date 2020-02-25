from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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
    ordering = ['-date_posted']


class NewsDetailView(DetailView):
    model = Post


class NewsCreateView(CreateView):
    model = Post  
    fields = ['title', 'content']

    def form_valid(self, from):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'livenews/about.html')
