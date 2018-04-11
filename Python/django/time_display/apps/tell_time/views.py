from django.shortcuts import render, HttpResponse, redirectrequest
from time import gmtime, strftime
  
def index(request):
    context = {
        "time": strftime("%b-%m-%Y %H:%M %p", gmtime())
    }
    return render(request, 'tell_time/index.html', context)