from django.shortcuts import render

def homepage(req):
    return render(req, 'pages/home.html')