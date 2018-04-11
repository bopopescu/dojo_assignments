from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'time' not in request.session:
        request.session['time'] = ''
    return render(request, 'game/index.html')

def process(request):
    if request.method == 'POST':
        building = request.POST['building']  
        request.session['time'] = strftime("%b-%m-%Y %H:%M %p", gmtime()) 
        if building == 'farm':
            ran_gold = random.randrange(10, 21)
            request.session['gold'] += ran_gold
            request.session['activity'].insert(0,("<p style='color:green'>Earned {} gold from the farm! ({})</p>".format(ran_gold,request.session['time'])))
            return redirect('/')
        if building == 'cave':
            ran_gold = random.randrange(5, 11)
            request.session['gold'] += ran_gold
            request.session['activity'].insert(0,("<p style='color:green'>Earned {} gold from the cave! ({})</p>".format(ran_gold,request.session['time'])))
            return redirect('/')
        if building == 'house':
            ran_gold = random.randrange(2, 6)
            request.session['gold'] += ran_gold
            request.session['activity'].insert(0,("<p style='color:green'>Earned {} gold from the house! ({})</p>".format(ran_gold,request.session['time'])))
            return redirect('/')
        if building == 'casino':
            odds = random.randrange(1, 3)
            print odds
            if odds == 1:
                ran_gold = random.randrange(0, 51)
                request.session['gold'] -= ran_gold
                request.session['activity'].insert(0,("<p style='color:red'>Ouch! Lost {} gold from the casino! ({})</p>".format(ran_gold,request.session['time'])))
                return redirect('/')
            else:
                ran_gold = random.randrange(0, 51)
                request.session['gold'] += ran_gold
                request.session['activity'].insert(0,("<p style='color:green'>Congrats! Won {} gold from the casino! ({})</p>".format(ran_gold,request.session['time'])))
                return redirect('/')
        return render_template('oops.html')
