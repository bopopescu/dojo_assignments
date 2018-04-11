from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
  
def index(request):
    return render(request, 'survey/index.html')


def process(request):
    if request.method == 'POST': 
        request.session['name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['favorite_language'] = request.POST['favorite_language'] 
        request.session['comment'] = request.POST['comment']
        if 'counter' not in request.session:
            request.session['counter'] = 1
        else:
            request.session['counter'] += 1
        return redirect("/result")



def result(request):
    return render(request, 'survey/result.html')
