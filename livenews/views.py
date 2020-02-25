from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Post  
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

 #Test for to allow the right user to update post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
#a delete view that allows the author to be able to delete the post
class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url ='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'livenews/about.html')
