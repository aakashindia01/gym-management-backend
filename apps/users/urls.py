from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.hello_user, name='hello_user'),
]