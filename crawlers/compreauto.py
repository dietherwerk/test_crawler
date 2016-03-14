# Framework imports
import requests
import bs4


class CompreautoCrawler(object):

    """
    Cralwer for Webmotors Site
    """

    def __init__(self, brand, model, init_year, final_year):
        super(CompreautoCrawler, self).__init__()
        self.brand = brand
        self.model = model
        self.init_year = init_year
        self.final_year = final_year

    def get_final_url(self):
        url = 'http://www.compreauto.com.br/buscar/tipo.carros-caminhonetes/marca.chevrolet/modelo.celta/tipo-veiculo.novos-usados/ano-de.2014/ano-ate.2016/anunciante.loja/?tipoveiculo=carro&anunciante=loja|concession%C3%A1ria|pessoa%20f%C3%ADsica&tipoanuncio=novos|usados&marca1=chevrolet&modelo1=celta&anode=2014&anoate=2016'
        return url

    def extract_data(self):
        response = requests.get(self.get_final_url())
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        arrayYears = []
        arrayColors = []
        arrayKm = []
        arrayCambio = []

        # KM
        details = soup.select('#anuncios .boxResultado .features div')
        for i, detail in enumerate(details):
            if i % 2 == 0:
                arrayYears.append(detail.select('span')[0].get_text())
                arrayColors.append(detail.select('span')[1].get_text())
            else:
                arrayKm.append(detail.select('span')[0].get_text())
                arrayCambio.append(detail.select('span')[1].get_text())

        # Links
        lk = 'http://www.compreauto.com.br'
        links = soup.select('#anuncios .boxResultado .tipo1')
        arrayLinks = [lk + link.get('href') for link in links]

        # Titles
        titles = soup.select('#anuncios .boxResultado .info h2')
        for title in titles:
            arrayTitles = [title.get_text().replace('\n', '') for title in titles]

        # Photos 
        photos = soup.select('#anuncios .boxResultado .photo img')
        arrayPhotos = [photo.get('data-original') for photo in photos]

        # Price
        prices = soup.select('#anuncios .boxResultado .photo .price')
        arrayPrices = [price.get_text().replace('\n', '').replace('\t', '').replace('\r', '') for price in prices]

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
