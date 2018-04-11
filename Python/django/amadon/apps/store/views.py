from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited

def index(request):
    return render(request, 'store/index.html')


def buy(request):''
    if request.method == 'POST':
        if 'tot_quan' not in request.session:
            request.session['tot_quan'] = int(0)
        if 'tot_cost' not in request.session:
            request.session['tot_cost'] = int(0)
        request.session['item'] = request.POST['product_id']
        request.session['quan'] = int(request.POST['quantity'])
        if request.session['item'] == '1':
            request.session['tot_quan'] += request.session['quan']
            request.session['quan'] *= float(19.99)
            request.session['tot_cost'] += request.session['quan']
        if request.session['item'] == '2':
            request.session['tot_quan'] += request.session['quan']
            request.session['quan'] *= float(29.99)
            request.session['tot_cost'] += request.session['quan']
        if request.session['item'] == '3':
            request.session['tot_quan'] += request.session['quan']
            request.session['quan'] *= float(4.99)
            request.session['tot_cost'] += request.session['quan']
        if request.session['item'] == '4':
            request.session['tot_quan'] += request.session['quan']
            request.session['quan'] *= float(49.99)
            request.session['tot_cost'] += request.session['quan']
        request.session['quan']
    return redirect('/amadon/checkout')

def checkout(request):
    return render( request, 'store/checkout.html')