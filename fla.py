from flask import render_template
from flask import Flask, request, jsonify, flash
from restfultools import *
import redis
r = redis.Redis(host='localhost', port=6379)

datas = [{'name': 'javascript', 'useto': 'web development'},
    {'name': 'python', 'useto': 'do anything'},
    {'name': 'php', 'useto': 'web development'},
    {'name': 'c++', 'useto': 'web server'}]

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def main(name=None):
    return render_template('index.html', name=name)

@app.route('/languages')
def getAll():
    return fullResponse(R200_OK, datas)

@app.route('/plus/<a1>/<a2>')
def plus(a1=0,a2=0):
    r.set('nx',a1)
    r.incr('nx',a2)
    ret = int(r.get('nx'))
    resp = {'result':ret}
    return fullResponse(R200_OK, resp)

@app.route('/login')
@app.route('/login/')
def login(username=None):
    return render_template('login.html')

@app.route('/api/login' , methods=['GET','POST'])
def api_login():
    username = request.json['username']
    password = request.json['password']
    if username == password:
        return statusResponse(R200_OK)
    else:
        return statusResponse(R403_FORBIDDEN)

if __name__ == '__main__':
    app.run()