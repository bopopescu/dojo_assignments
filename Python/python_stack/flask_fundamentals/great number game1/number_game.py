from flask import Flask, render_template, redirect, session, request
import random


app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'secret_number' not in session:
        session['secret_number'] = random.randrange(1, 101)
    print session['secret_number']
    return render_template("index.html")


@app.route('/guess', methods=["POST"])
def num_guess():
    if request.method == 'POST':
        guess = int(request.form['number'])

        if guess > session['secret_number']:
            print session['secret_number']
            print guess
            print "greater"
            return render_template('too_high.html')
            # return render_template("you_win.html")
        elif guess < session['secret_number']:
            print session['secret_number']
            print "less"
            print guess
            return render_template('too_low.html')
        elif guess == session['secret_number']:
            print session['secret_number']
            print guess
            return render_template('you_win.html')
    return redirect('/')


@app.route('/again', methods=['GET', 'POST'])
def again():
    session.pop('secret_number')
    return redirect('/')


app.run(debug=True)
