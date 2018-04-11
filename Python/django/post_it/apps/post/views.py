from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    context = {
        'posts' : Post_it.objects.all()
    }
    return render(request, ('post/index.html'), context)


def post(request):
    if request.method == 'POST':
        Post_it.objects.create(content=request.POST['content'])
        return redirect('/')