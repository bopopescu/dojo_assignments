from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emailsdb')
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("The email address you entered {} is a VALID email address! Thank you!".format(request.form['email']))
        query = "INSERT INTO emails (emails, created_at) VALUES (:email, NOW())"
        data = {
            'email' : request.form['email'],
        }
        mysql.query_db(query, data)
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def success():
    
    query = "SELECT * FROM emails" 
    emails = mysql.query_db(query)  
    for people in emails:   
        people['created_at'] = people['created_at'].strftime('%b %d %Y')
    return render_template('success.html', email=emails,)



app.run(debug=True)