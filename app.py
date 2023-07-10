from flask import Flask
app = Flask(__name__)

# setting routes

@app.route('/')
def index():
    return 'índice'

@app.route('/hello')
def hello():
    return 'segunda ruta'