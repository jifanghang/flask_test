from flask import Flask, redirect, render_template, request, request, url_for, flash
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('Login.html', error = error)

if __name__ == "__main__":
    app.run(debug = True)