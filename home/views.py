from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Question


def home(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html', {'title': 'about'})
