# Flask - Template

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return '<html><body><h1>Hello World</h1></body></html>'
    return render_template('hello.html')

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)

@app.route('/hello/<int:score>')
def hello_score(score):
    return render_template('hello.html', marks = score)

@app.route('/result')
def result():
    results = {'phy':50, 'che':60, 'maths':70}
    return render_template('result.html', result = results)

if __name__ == '__main__':
    app.run(debug = True)
