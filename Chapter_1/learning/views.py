from django.http import HttpResponse
from django.shortcuts import render

def homepage(req):
    # return HttpResponse("Home Page")
    return render(req, "home.html")

def aboutpage(req):
    # return HttpResponse("This is about page")
    return render(req, "about.html")