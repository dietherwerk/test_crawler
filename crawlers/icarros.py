# Framework imports
import requests
import bs4


class IcarrosCrawler(object):

    """
    Cralwer for Webmotors Site
    """

    def __init__(self, brand, model, init_year, final_year):
        super(IcarrosCrawler, self).__init__()
        self.brand = brand
        self.model = model
        self.init_year = init_year
        self.final_year = final_year

    def get_final_url(self):
        url = 'http://www.icarros.com.br/ache/listaanuncios.jsp?bid=0&opcaocidade=1&foa=1&anunciosNovos=1&anunciosUsados=1&marca1=15&modelo1=283&anomodeloinicial=2013&anomodelofinal=2016&precominimo=0&precomaximo=0&cidadeaberto=&escopo=2&locationSop=cid_9668.1_-est_SP.1_-esc_2.1_-rai_25.1_'
        return url

    def extract_data(self):
        response = requests.get(self.get_final_url())
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        arrayPhotos = []

        # Year
        years = soup.select('.lista_anuncios .anuncios .anuncio_container .dados_veiculo .primeiro p')
        arrayYears = [year.get_text() for year in years]

        # KM
        kms = soup.select('.lista_anuncios .anuncios .anuncio_container .dados_veiculo .usado p')
        arrayKm = [km.get_text().replace('\r\n', '').replace(' ', '') for km in kms]

        # Colors
        colors = soup.select('.lista_anuncios .anuncios .anuncio_container .dados_veiculo . p')
        arrayColors = [color.get_text() for color in colors]

        # Cambio
        cambios = soup.select('.lista_anuncios .anuncios .anuncio_container .dados_veiculo .ultimo p')
        arrayCambio = [cambio.get_text() for cambio in cambios]

        # Links
        icarrosURL = "http://www.icarros.com.br"
        links = soup.select('.lista_anuncios .anuncios .anuncio_container .dados_veiculo a')
        arrayLinks = [icarrosURL + link.get('href') for link in links]

        # Titles              .lista_anuncios .anuncios .anuncio_container titulo_anuncio
        titles = soup.select('.lista_anuncios .anuncios .anuncio_container .titulo_anuncio')
        arrayTitles = [title.get_text() for title in titles]

        # Photos
        photos = soup.select('.lista_anuncios .anuncios .anuncio_container .dados_anuncio .imglazy')
        for photo in photos:
            image = photo.get('src')
            if image is None:
                image = photo.get('data-src')

            arrayPhotos.append(image)

        # Price
        prices = soup.select('.lista_anuncios .anuncios .anuncio_container .preco_anuncio')
        arrayPrices = [price.get_text() for price in prices]

        arrayFinal = []

        # create the dict
        for i, photo in enumerate(arrayPhotos):
            car = {'title': arrayTitles[i],
                   'link': arrayLinks[i],
                   'photo': arrayPhotos[i],
                   'price': arrayPrices[i],
                   'year': arrayYears[i],
                   'color': arrayColors[i],
                   'km': arrayKm[i],
                   'cambio': arrayCambio[i]
                   }
            arrayFinal.append(car)

        return arrayFinal
