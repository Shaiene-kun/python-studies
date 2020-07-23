from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Class views
class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"

class ArticleView(DetailView):
    model = Post
    template_name = "posts/article-detail.html"

def base(request):
    return render(request,'base/base.html',{})

# Create your views here.

# Function Views
# def home(request):
#     return render(request,'home.html', {})
