from django.shortcuts import render
from .forms import TeacherForm
from .models import Teacher

# Create your views here.
def app(request):
    return render(request, 'app.html')


def login(request):
    return render(request, 'login.html')




def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    return render(request, 'register.html')


def Teach(request):
    form=TeacherForm()
    return render(request, '/Teach.html')