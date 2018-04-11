from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
  
def index(request):
   
    return render(request, 'name_gen/index.html')


def generate(request):
    print '*'*50
    if 'counter' not in request.session
    else:
        request.session['counter'] += 1

    print request.session['counter']
    
    context = {
        'random_word': get_random_string(length=14)
    }
    return render(request, 'name_gen/index.html', context)


def reset(request):
    request.session['counter'] = 1
    return redirect ('/')