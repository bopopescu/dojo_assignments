from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
  
from models import *


def index(request):
   
    return render(request, ('users/index.html'), { 'users' : User.objects.all()})


def create(request):
    
    return render(request, ('users/create.html'))


def process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    if request.method == 'POST':
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])       

    return redirect('/users')
 

def edit(request, id):
    request.session['id'] = id
    return render(request, 'users/edit.html', { 'user' : User.objects.get(id = id)})


def update(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/'+request.POST['id']+'/edit')
    if request.method == 'POST':
        up = User.objects.get(id = request.POST['id'])
        up.first_name = request.POST['first_name']
        up.last_name = request.POST['last_name']
        up.email = request.POST['email']
        up.save()
        return redirect('/users/'+request.POST['id'])


def show(request, id):
    request.session['id'] = id
    return render( request, 'users/show.html', { 'user' : User.objects.get(id=id)})


def delete(request, id):
    request.session['id'] = id
    d = User.objects.get( id = request.session['id'])
    d.delete()
    return render(request, 'users/index.html', { 'users' : User.objects.all()})