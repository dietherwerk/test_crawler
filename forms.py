# coding: utf-8

# Framework Imports
from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import Required


class CarForm(Form):
    brand = SelectField('brand',
                        choices=[('ford', 'Ford'),
                                 ('fiat', 'Fiat'),
                                 ('chevrolet', 'Chevrolet')], validators=[Required()])

    model = SelectField('model',
                        choices=[('ranger', 'Ranger'),
                        		 ('fiesta', 'Fiesta'),	
                        		 ('palio', 'Palio'),
                                 ('stilo', 'Stilo'),
                                 ('astra', 'Astra'),
                                 ('celta', 'Celta')], validators=[Required()])

    inityear = SelectField('year',
                        choices=[('2010', '2010'),
                                 ('2011', '2011'),
                                 ('2012', '2012'),
                                 ('2013', '2013'),
                                 ('2014', '2014'),
                                 ('2015', '2015')], validators=[Required()])

    finalyear = SelectField('year',
                        choices=[('2010', '2010'),
                                 ('2011', '2011'),
                                 ('2012', '2012'),
                                 ('2013', '2013'),
                                 ('2014', '2014'),
                                 ('2015', '2015')],validators=[Required()])
