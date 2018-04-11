from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ninja')
def ninja():
    return render_template("ninja.html")


@app.route('/ninja/<color>')
def turtle(color):
    turtle = ""
    
    if color == 'red':
        turtle = 'red.jpg'
    elif color == 'blue':
        turtle = 'blue.jpg'
    elif color == 'orange':
        turtle = 'orange.jpg'
    elif color == 'purple':
        turtle = 'purple.jpg'
    else:
        turtle = 'notapril.jpg'
    
    return render_template('turtle.html', turtle=turtle)
    


app.run(debug=True)



