# Framework imports
from flask import url_for, flash, render_template, request, redirect, session, jsonify, make_response
from app import app
from forms import CarForm
from helpers import extract_data


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()

    return render_template('index.html', form=form)


@app.route('/result/', methods=['POST'])
def result():
    url = 'http://www.webmotors.com.br/comprar/carros/novos-usados/'
    url = url + 'veiculos-todos-estados/{brand}/{model}/?tipoveiculo=carros'
    url = url + '&tipoanuncio=novos|usados&marca1={brand}&modelo1={model}'
    url = url + '&anode={inityear}&anoate={finalyear}&estado1=veiculos-todos-estados'
    url = url.format(brand=request.form['brand'], 
    	             model=request.form['model'],
    	             inityear=request.form['inityear'],
    	             finalyear=request.form['finalyear'])


    cars = extract_data(url)

    return render_template('result.html', cars=cars)    