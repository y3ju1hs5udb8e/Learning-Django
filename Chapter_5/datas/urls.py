from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_page, name='list'),
    path('<slug:slug>', views.sigle_post, name='single')
]
