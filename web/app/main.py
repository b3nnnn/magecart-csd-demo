from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

javascript = '<script src="' + os.environ.get('JSURI') + '"></script>'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/payment-page.html')
def pay():
    return render_template('payment-page.html',javascript=javascript)



@app.route('/assets/<path:path>')
def send_asset(path):
    print(path)
    return send_from_directory('static', path)

