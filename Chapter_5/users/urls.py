from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('resgister/', views.registerpage, name='register')
]
