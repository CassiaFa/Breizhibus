from http import client
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/affiche_bus')
def affiche_bus():
    return render_template('affiche_bus.html')

@app.route('/add', methods=['get'])
def add():
    
    return render_template('add.html')

if __name__== "__main__" :
    app.run(debug=True, port=5001)