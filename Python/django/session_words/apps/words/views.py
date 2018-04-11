from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'words/index.html')

def process(request):
    if request.method == 'GET':
        request.session['word'] = request.GET['word']
        request.session['color'] = request.GET['color']
        request.session['date'] = strftime("%b-%m-%Y %H:%M %p", gmtime())
        if 'big' not in request.GET:
            request.session['big'] = '1em'
        else:
            request.session['big'] = request.GET['big']
    else:
        return redirect('/')
    
    if 'activity' not in request.session:
        request.session['activity'] = ''
    
    if 'time' not in request.session:
        request.session['time'] = ''

    request.session['time'] += '<p>added on{}</p>'.format(request.session['date'])
   
    request.session['activity'] += "<p><span style='color:{};font-size:{};'>{}</span></p>".format(request.session['color'],request.session['big'],request.session['word'])
    return render(request, 'words/index.html')


def clear(request):
    request.session.clear()
    return redirect('/')