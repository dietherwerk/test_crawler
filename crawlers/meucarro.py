# Framework imports
import requests
import bs4


class MeucarroCrawler(object):

    """
    Cralwer for Webmotors Site
    """

    def __init__(self, brand, model, init_year, final_year):
        super(MeucarroCrawler, self).__init__()
        self.brand = brand
        self.model = model
        self.init_year = init_year
        self.final_year = final_year

    def get_final_url(self):
        url = 'https://www.meucarronovo.com.br/carros/q/CHEVROLET AGILE/ano-min/2010/ano-max/2016/origem/combo-home'
        return url

    def extract_data(self):
        response = requests.get(self.get_final_url())
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        arrayYears = []
        arrayColors = []
        arrayKm = []
        arrayPhotos = []

        # Year / Km / Color
        years = soup.select('.marg-t-30 .bg-card .w-300 a .txt-12')
        for i, year in enumerate(years):
            if i % 2 != 0:
                data = year.get_text().encode('utf-8').replace('\n', '').replace('\t', '')
                data = data.replace('\xa0', '').replace('\xc2', '').replace(" ", '').split('|')
                arrayColors.append(data[0])
                arrayKm.append(data[2])
                arrayYears.append(data[3])

        # Titles
        titles = soup.select('.marg-t-30 .bg-card .w-300 a .txt-18')
        arrayTitles = [title.get_text() for title in titles]

        # Links
        links = soup.select('.col-lg-6 .bg-card .w-180 a')
        arrayLinks = [link.get('href') for link in links]

        # Photos
        photos = soup.select('.col-lg-6 .bg-card .w-180 a img')
        for photo in photos:
            image = photo.get('src').replace('\n', '').replace('\t', '')
            image = image.replace('https://d1x1xhcjqq6e69.cloudfront.net/fotos/veiculos/', 
                                  'https://d1x1xhcjqq6e69.cloudfront.net/imagens-dinamicas/detalhe-veiculo-grande/fotos/veiculos/')
            image = image.replace('_busca', '')

            arrayPhotos.append(image)

        # Price
        prices = soup.select('.marg-t-30 .bg-card .w-300 a .txt-13')
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
                   'km': arrayKm[i]
                   }
            arrayFinal.append(car)

        return arrayFinal
