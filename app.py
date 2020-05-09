from flask import Flask, request, render_template, url_for, redirect
from lista_palabras import dicc_esp_qu

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/word', methods=['POST'])
def form_sended():
    word_origin = request.form['searchname']
    word = word_origin.lower()
    try:
        result = dicc_esp_qu[word]
        return render_template('result.html', result = result)
    except KeyError:
        result = "No encontramos la palabra que buscas, fijate en los errores ortográficos."
        return render_template('result.html', result = result)
    