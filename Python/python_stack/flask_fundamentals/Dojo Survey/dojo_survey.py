from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if len(request.form['name']) < 1:
            flash('Name cannot be blank!')
        else:
            flash('Success!')
            return render_template("user_info.html", form=request.form)
    return render_template('index.html')


app.run(debug=True)
