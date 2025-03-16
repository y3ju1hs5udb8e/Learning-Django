from django.shortcuts import render

# home page view
def homepage(req):
    return render(req, 'home.html')

# about page view
def aboutpage(req):
    return render(req, 'about.html')