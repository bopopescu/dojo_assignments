from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
import datetime


app = Flask(__name__)
mysql = MySQLConnector(app,'friendsassbd')


@app.route('/')
def index():
    query = "SELECT name, age, created_at FROM friends" 
    friends = mysql.query_db(query)  
    # print friends
    for people in friends:   
        people['created_at'] = people['created_at'].strftime('%b %d %Y')


    return render_template('index.html', friend=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (name, age, created_at) VALUES (:name, :age, NOW())"
    data={
        'name' : request.form['name'],
        'age' : request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)