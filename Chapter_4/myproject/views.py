from django.shortcuts import render

def homepage(req):
    return render(req, 'pages/home.html')

def aboutpage(req):
    return render(req, 'pages/about.html')