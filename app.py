# coding: utf-8
# Framework imports
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

import views
