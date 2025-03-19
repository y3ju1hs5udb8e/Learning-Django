from django.shortcuts import render
from .models import Posts

posts = Posts.objects

# Create your views here.
def postlistpage(req):
    return render(req, 'posts.html', {'posts': posts.all().order_by('-date')})

def singlepost(req, slug):
    return render(req, 'single_post.html', {'post': posts.get(slug=slug)})