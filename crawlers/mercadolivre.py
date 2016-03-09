# Framework imports
import requests
import bs4


class MercadolivreCrawler(object):

    """
    Cralwer for MercadolivreCrawler Site
    """

    def __init__(self, brand, model, init_year, final_year):
        super(MercadolivreCrawler, self).__init__()
        self.brand = brand
        self.model = model
        self.init_year = init_year
        self.final_year = final_year

    def get_final_url(self):
        url = 'http://carros.mercadolivre.com.br/'
        url = url + '{brand}/{model}_YearRange_{init_year}-{final_year}#D[H:true]'
        url = url.format(brand=self.brand,
                         model=self.model,
                         init_year=self.init_year,
                         final_year=self.final_year)

        return url

    def extract_data(self):
        response = requests.get(self.get_final_url())
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # setting arrays
        arrayYear = []
        arrayKm = []

        # Year and KM
        years_km = soup.select('#searchResults .article .details .destaque')
        for year_km in years_km:
            year_km = year_km.get_text()
            year_km = year_km.encode('utf8')
            year_km = year_km.replace('\xc2', '')
            year_km = year_km.replace('\xa0', '')
            year_km = year_km.replace(' ', '')
            year_km = year_km.split('|')
            arrayYear.append(year_km[0])
            arrayKm.append(year_km[1]) 

        # Prices
        prices = soup.select('#searchResults .article .details .costs .ch-price')
        arrayPrices = [price.get_text() for price in prices]

        # Titles
        data_title_links = soup.select('#searchResults .article .list-view-item-title . ')
        arrayTitles = [data_title_link.get_text() for data_title_link in data_title_links]

        # Links
        arrayLinks = [data_title_link.get('href') for data_title_link in data_title_links]

        # Photos
        photos = soup.select('#searchResults .article .images-viewer .item-link noscript img')
        arrayPhotos = [photo.get('src') for photo in photos]

        # Price
        prices = soup.select('#searchResults .article .details .costs .ch-price')
        arrayPrices = [price.get_text() for price in prices]

        arrayFinal = []

        # create the dict
        for i, photo in enumerate(arrayPhotos):
            car = {'title': arrayTitles[i],
                   'link': arrayLinks[i],
                   'photo': arrayPhotos[i],
                   'price': arrayPrices[i],
                   'year': arrayYear[i],
                   'km': arrayKm[i]
                   }
            arrayFinal.append(car)

        return arrayFinal
