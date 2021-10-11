from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author':'Mahmoud',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted':'Augest 23, 2019'
    },
    {
        'author':'Ahmed',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted':'Augest 24, 2019'
    }
]
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'my_blog/home.html', context)


def about(request):
    return render(request, 'my_blog/about.html')
