from django.shortcuts import render

from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'Fuad Suleymanov',
#         'title': 'Blog Post1',
#         'content': 'First post content',
#         'date_posted': '01.12.2020'
#     },
#     {
#         'author': 'Cavid Balayev',
#         'title': 'Blog Post2',
#         'content': 'Second post content',
#         'date_posted': '30.11.2020'
#     },
# ]

posts = Post.objects.all()

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})