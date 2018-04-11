from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):

    return render(request, ('register/index.html'), { 'courses' : Course.objects.all()} )


def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    if request.method == 'POST':
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])  
    return redirect('/')   


def delete(request, id):
    return render(request, ('register/destroy.html'), { 'course' : Course.objects.get(id=id)} )


def destroy(request, id):
    d = Course.objects.get( id = id)
    d.delete()
    return redirect('/')