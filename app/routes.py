from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/result', methods=['POST'])
def result():
    projectpath = request.form['projectFilepath']
    # your code
    # return a response