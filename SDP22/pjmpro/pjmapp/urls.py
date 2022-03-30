from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('register',views.register,name="register"),
    path('Teach',views.Teach,name="Teach"),
]
