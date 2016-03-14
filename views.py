# Framework imports
from flask import render_template, request
from app import app
from forms import CarForm
from crawlers.webmotors import WebmotorsCrawler
from crawlers.mercadolivre import MercadolivreCrawler
from crawlers.olx import OlxCrawler
from crawlers.icarros import IcarrosCrawler
from crawlers.meucarro import MeucarroCrawler
from crawlers.compreauto import CompreautoCrawler


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()

    return render_template('index.html', form=form)


@app.route('/result/', methods=['POST'])
def result():
    webmotors = WebmotorsCrawler(request.form['brand'],
                                 request.form['model'],
                                 request.form['inityear'],
                                 request.form['finalyear'])

    mercadolivre = MercadolivreCrawler(request.form['brand'],
                                       request.form['model'],
                                       request.form['inityear'],
                                       request.form['finalyear'])

    olx = OlxCrawler(request.form['brand'],
                     request.form['model'],
                     request.form['inityear'],
                     request.form['finalyear'])

    icarros = IcarrosCrawler(request.form['brand'],
                             request.form['model'],
                             request.form['inityear'],
                             request.form['finalyear'])

    meucarro = MeucarroCrawler(request.form['brand'],
                               request.form['model'],
                               request.form['inityear'],
                               request.form['finalyear'])

    compreauto = CompreautoCrawler(request.form['brand'],
                                   request.form['model'],
                                   request.form['inityear'],
                                  request.form['finalyear'])

    return render_template('result.html',
                           webmotors=webmotors.extract_data(),
                           mercadolivre=mercadolivre.extract_data(),
                           olx=olx.extract_data(),
                           icarros=icarros.extract_data(),
                           meucarro=meucarro.extract_data(),
                           compreauto=compreauto.extract_data())
