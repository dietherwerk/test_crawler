# Framework imports
import requests
import bs4


class WebmotorsCrawler(object):

    """
    Cralwer for Webmotors Site
    """

    def __init__(self, brand, model, init_year, final_year):
        super(WebmotorsCrawler, self).__init__()
        self.brand = brand
        self.model = model
        self.init_year = init_year
        self.final_year = final_year

    def get_final_url(self):
        url = 'http://www.webmotors.com.br/comprar/carros/novos-usados/'
        url = url + 'veiculos-todos-estados/{brand}/{model}/?tipoveiculo=carros'
        url = url + '&tipoanuncio=novos|usados&marca1={brand}&modelo1={model}'
        url = url + '&anode={init_year}&anoate={final_year}&estado1=veiculos-todos-estados'
        url = url.format(brand=self.brand,
                         model=self.model,
                         init_year=self.init_year,
                         final_year=self.final_year)

        return url

    def extract_data(self):
        response = requests.get(self.get_final_url())
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # setting arrays
        arrayPrices = []
        arrayYear = []
        arrayColors = []
        arrayKm = []
        arrayCambio = []

        # Details
        details = soup.select('div#anuncios .tipo1 .info .features')
        for detail in details:
            text = detail.get_text()
            text = text.replace('\n\n', "")
            text = text.split('\n')
            arrayYear.append(text[0])
            arrayColors.append(text[1])
            arrayKm.append(text[2])
            arrayCambio.append(text[3])

        # Links
        links = soup.select('div#anuncios .tipo1')
        arrayLinks = [link.get('href') for link in links]

        # Titles
        titles = soup.select('div#anuncios .tipo1 .info .make-model')
        arrayTitles = [title.get_text() for title in titles]

        # Subtitles
        subtitles = soup.select('div#anuncios .tipo1 .info .version')
        arraySubtitles = [subtitle.get_text() for subtitle in subtitles]

        # Photos
        photos = soup.select('div#anuncios .c-after .photo img')
        arrayPhotos = [photo.get('data-original') for photo in photos]

        # Price
        prices = soup.select('div#anuncios .c-after .photo .price')

        for price in prices:
            text = price.get_text()
            text = text.replace('\n', "")
            text = text.replace('\r', "")
            text = text.replace('\t', "")

            arrayPrices.append(text)

        arrayFinal = []

        # create the dict
        for i, photo in enumerate(arrayPhotos):
            car = {'title': arrayTitles[i],
                   'subtitle': arraySubtitles[i],
                   'link': arrayLinks[i],
                   'photo': arrayPhotos[i],
                   'price': arrayPrices[i],
                   'year': arrayYear[i],
                   'color': arrayColors[i],
                   'km': arrayKm[i],
                   'cambio': arrayCambio[i]
                   }
            arrayFinal.append(car)

        return arrayFinal
