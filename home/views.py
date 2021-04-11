from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def home(request):
#     return HttpResponse('<h1> CodePanda Home</h1>')

posts = [
    {
        'question': 'reverse of an array',
        'title': 'array',
        'date_posted': '21 May,2018'
    },
    {
        'question': 'height of a binary tree',
        'title': 'trees',
        'date_posted': '11 Aug,2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html', {'title': 'about'})
