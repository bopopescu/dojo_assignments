from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
import re
import md5
import os, binascii


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'walldb')
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/log_in', methods=['POST'])
def log_in():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
        data = {'email': email}
        user = mysql.query_db(query, data)
        if len(user) !=0:
            session['user'] = user
            print user
            encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
            if user[0]['password'] == encrypted_password:
                return redirect('/wall')
            else:
                flash('Incorrect Password')
                return redirect('/')
        else:
            flash('Email not in database. Please register!')
            return redirect('/register')

@app.route('/process', methods=['POST'])
def process_reg():
    error_messages =[]
    if len(request.form['first_name']) < 2 and (request.form['first_name'].isalpha() != True):
        error_messages.append("First name must be at least 2 characters and contain only letters")
    if len(request.form['last_name']) < 2 or (request.form['last_name'].isalpha() != True):
        error_messages.append("Last name must be at least 2 characters and contain only letters")
    if not EMAIL_REGEX.match(request.form['email']):
        error_messages.append("Invalid Email Address")
    if len(request.form['password']) < 8:
        error_messages.append("Password must be 8 characters long")
    if request.form['password'] !=  request.form['confirm_password']:
        error_messages.append("Passwords must match")
    
    if not error_messages:
        flash('Registration Successful!')
        password = request.form['password']
        salt =  binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()
        query = 'INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW())'
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'hashed_pw' : hashed_pw,
            'salt' : salt
        }
        mysql.query_db(query, data)
        return redirect('/')
    else:
        for message in error_messages:
            flash(message)
        error_messages = []
        return redirect ('/register')

    return redirect ('/register')


@app.route('/wall')
def success():
    query = "SELECT * FROM messages LEFT JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(query)
    query1 = "SELECT * FROM comments LEFT JOIN users ON users.id = comments.user_id LEFT JOIN messages ON messages.m_id = comments.message_id ORDER BY comments.created_at ASC"
    comments = mysql.query_db(query1)
    query2 = "SELECT * FROM users"
    users = mysql.query_db(query2)
    return render_template('wall.html', message = messages, comment = comments, user = users)


@app.route('/post_message', methods=['POST'])
def post_message():
    query = "INSERT INTO messages (mess_content, user_id) VALUES (:content, :user)"
    data = {
        'content' : request.form['mess_content'],
        'user' : session['user'][0]['id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/post_comment', methods=['POST'])
def post_comment():
    query = "INSERT INTO comments (com_content, user_id, message_id) VALUES (:content, :user, :message)"
    data = {
        'content' : request.form['com_content'],
        'user' : session['user'][0]['id'],
        'message' : request.form['mess_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/log_out')
def log_out():
    session.clear()
    return redirect ('/')

app.run(debug=True)