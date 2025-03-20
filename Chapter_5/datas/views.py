from django.shortcuts import render
from .models import BlogPosts

blogpost = BlogPosts.objects

# Create your views here.
def posts_page(req):
    return render(req, 'posts.html', {'posts': blogpost.all()})

def sigle_post(req, slug):
    return render(req, 'single_post.html', {'post': blogpost.get(slug=slug)})