from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {'author': 'lorca',
     'title': 'dummy post',
     'content': 'test bla bla bla lorem ipsum',
     'date_proceded': 2021},

    {'author': 'somebody',
     'title': 'not important',
     'content': 'lorem ipsum',
     'date_proceded': 2020}
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

