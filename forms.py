# coding: utf-8

# Framework Imports
from flask_wtf import Form
from wtforms import SelectField, SubmitField


class CarForm(Form):
    brand = SelectField('brand',
                        choices=[('Ford', 'ford'),
                                 ('Fiat', 'fiat'),
                                 ('Chevrolet', 'chevrolet')])

    model = SelectField('model',
                        choices=[('Palio', 'palio'),
                                 ('Uno', 'uno'),
                                 ('Fiesta', 'fiesta')])

    year = SelectField('year',
                        choices=[('2010', '2010'),
                                 ('2011', '2011'),
                                 ('2012', '2012'),
                                 ('2013', '2013'),
                                 ('2014', '2014'),
                                 ('2015', '2015')])
