from django.shortcuts import render
from .models import Posts

# Create your views here.
def posts(req):
    posts = Posts.objects.all().order_by('-date')
    return render(req, 'posts.html', {'posts': posts})