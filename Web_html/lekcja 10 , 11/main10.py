from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Alex'
    lista = ['Jajka', 'Mleko', 'Chleb', 'Masł', 'Szyka']
    slownik = {
        'red': 'czerony',
        'blue': 'niebieski',
        'green': 'zielony'

    }
    return  render_template('index3.html', name=name, lista=lista, slownik=slownik)

app.run(debug=True)