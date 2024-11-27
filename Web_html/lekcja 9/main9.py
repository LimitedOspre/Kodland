from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Igor"
    liste = ['Java', 'Python', 'C++', 'C#', 'JavaScript']
    slownik = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL": "odpowiedź na żart",
            "SHEESH": "lekka dezaprobata",
            "CREEPY": "straszny, złowieszczy",
            }
    return f'''
               <h1>Hello, {name}</h1>
               <p>Welcome to my first Flask app! </p>
               <h2> Ulubiony język to: {random.choice(liste)} </h2>
               <h3> {slownik['LOL']} </h3>
               <ul>
               <li> <a href="/druga"> druga strona </a> </li>
               <li> <a href="/trzecia"> trzecia strona </a> </li>
               <li> <a href="/cztery"> czwarta strona </a> </li>
               </ul>
            '''

@app.route("/druga")
def druga():
    return '''
               <h2> Druga strona </h2>
               <ul>
                    <li> <a href="/"> Main strona </a> </li>
                    <li> <a href="/trzecia"> trzecia strona </a> </li>
               </ul>
            '''

@app.route("/trzecia")
def trzecia():
    return '''
            <h2> Trzecia strona </h2>
            <ul>
                <li> <a href="/"> Main strona </a> </li>
                <li> <a href="/druga"> druga strona </a> </li>
            </ul>
            <img src= "static/back.jpg" alt="back" width=400" height='400'>
            '''

@app.route("/cztery")
def czwarta():
    ciekaw = [ 'Pigliny chodź są netherowymi mobami palą się w lawie.','Uderzając krowe w głowe nie zadacie jej obrażeń.','Klawiszami f3 + g możemy zobaczyć chanki.','Nie trzeba wchodzic w ustawienia gry żeby zmienić pole widzenia można to zrobić klawiszami  f3 + f.','Nie trzeba też wpisywać /gamemode  żeby zmienić tryb gry można to zrobic skrótem f3 + n.','W starszych wersjach kamień dało się wykopać łapką.','Dawniej szkielety nie miały łuku.']
    return f'''
            <h2> czwatrta strona - strona o MINECRAFT</h2>
            <ul>
                <li> <a href="/"> Main strona </a> </li>
            </ul>
            <img src= "static/mine.jpg" alt="back" width=350" height='190'>
            <h4> losowa ciekawostka o MINECRAFT: {random.choice(ciekaw)}</h4>
            '''

app.run(debug=True)