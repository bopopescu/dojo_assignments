from flask import Flask, render_template, redirect, session, request
import random


app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = ''
    return render_template('index.html', gold=session['gold'],activity=session['activity'])


@app.route('/process_money', methods=['POST'])
def process_money():
    if request.method == 'POST':
        building = request.form['building']   #request.form  #how did i get location name
        # session['activity'] = '' #this clear activity every push of submit
        print building
        if building == 'farm':       #farm
            ran_gold = random.randrange(10, 21)
            session['gold'] += ran_gold
            session['activity'] += '<p>Earned {} gold from the farm!</p>'.format(ran_gold)
            return redirect('/')
        if building == 'cave':     #cave
            ran_gold = random.randrange(5, 11)
            session['gold'] += ran_gold
            session['activity'] += '<p>Earned {} gold from the cave!</p>'.format(ran_gold)
            return redirect('/')
        if building == 'house':       #house
            ran_gold = random.randrange(2, 6)
            session['gold'] += ran_gold
            session['activity'] += '<p>Earned {} gold from the house!</p>'.format(ran_gold)
            return redirect('/')
        if building == 'casino':         #casino
            odds = random.randrange(1, 3)
            print odds
            if odds == 1:
                ran_gold = random.randrange(0, 51)
                session['gold'] -= ran_gold
                session['activity'] += '<p>Ouch! Lost {} gold from the casino!</p>'.format(ran_gold)
                return redirect('/')
            else:
                ran_gold = random.randrange(0, 51)
                session['gold'] += ran_gold
                session['activity'] += '<p>Congrats! Won {} gold from the casino!</p>'.format(ran_gold)
                return redirect('/')
        return render_template('oops.html')


app.run(debug=True)
