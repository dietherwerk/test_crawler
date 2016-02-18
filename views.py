# Framework imports
from flask import url_for, flash, render_template, request, redirect, session, jsonify, make_response
from app import app
from forms import CarForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()

    if form.validate_on_submit():
        pass

    return render_template('index.html', form=form)


@app.route('/result/', methods=['GET', 'POST'])
def result():
    return render_template('result.html')    