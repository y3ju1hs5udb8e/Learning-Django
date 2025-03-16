from django.shortcuts import render

# Create your views here.
def posts(req):
    return render(req, 'posts.html')