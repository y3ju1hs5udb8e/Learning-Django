from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.postlistpage, name='list'),
    path('<slug:slug>', views.singlepost, name='post')
]