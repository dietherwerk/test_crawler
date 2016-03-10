# Framework imports
# -*- coding: utf-8 -*- 
import requests
import bs4


class OlxCrawler(object):

    """
    Cralwer for Olx Site
    """

    YEARS = {
        '2016': '34',
        '2015': '33',
        '2014': '32',
        '2013': '31',
        '2012': '30',
        '2011': '29',
        '2010': '28',
        '2009': '27',
        '2008': '26',
        '2007': '25',
        '2006': '24',
        '2005': '23',
        '2004': '22',
        '2003': '21',
        '2002': '20',
        '2001': '19',
        '2000': '18'
    }

    def __init__(self, brand, model, init_year, final_year):
        super(OlxCrawler, self).__init__()
        self.brand = brand
        self.model = model
        self.init_year = init_year
        self.final_year = final_year

    def get_final_url(self):
        url = 'http://olx.com.br/veiculos/carros/{brand}/{model}?re={init_year}&rs={final_year}'
        url = url.format(brand=self.brand,
                         model=self.model,
                         init_year=self.YEARS.get(self.init_year),
                         final_year=self.YEARS.get(self.final_year))

        return url

    def extract_data(self):
        response = requests.get(self.get_final_url())
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # setting arrays
        arrayYears = []
        arrayKm = []
        arrayCambio = []
        arrayTitles = []
        arrayPhotos = []
        ArrayPrices = []

        # KM
        details = soup.select('.section_OLXad-list .item .OLXad-list-line-1 .detail-specific')
        for detail in details:
            detail = detail.get_text().replace('\n', '').replace('\t', '').encode('utf8')
            detail = detail.replace('\xc3\xa2', 'a').replace('\xa1', 'a')
            detail = detail.split('|')
            arrayKm.append(detail[0])
            arrayCambio.append(detail[1].replace('\xc3a', 'a'))

        # Links
        links = soup.select('.section_OLXad-list .item a')
        arrayLinks = [link.get('href') for link in links]

        # Titles / Year
        titles_years = soup.select('.section_OLXad-list .item .OLXad-list-line-1 .OLXad-list-title')
        for title_year in titles_years:
            title = title_year.get_text().replace('\n', '').replace('\t', '').split('-')[0]
            year = title_year.get_text().replace('\n', '').replace('\t', '').split('-')[1]

            arrayTitles.append(title)
            arrayYears.append(year)

        # Photos 
        photos = soup.select('.section_OLXad-list .item .OLXad-list-image .OLXad-list-image-box')
        for photo in photos:
            try:
                image = photo.select('img')[0]
                original = image.get('data-original')
                if original is None:
                    image = image.get('src')
                else:
                    image = original
                image = image.replace('thumbsli', 'images')
            except IndexError:
                image = None
            arrayPhotos.append(image)

        # Price
        items = soup.select('.section_OLXad-list .item')
        for item in items:
            try:
                price = item.select('.OLXad-list-price')[0].get_text()
            except IndexError:
                price = '0'
            ArrayPrices.append(price)

        arrayFinal = []

        # create the dict
        for i, photo in enumerate(arrayPhotos):
            car = {'title': arrayTitles[i],
                   'link': arrayLinks[i],
                   'photo': arrayPhotos[i],
                   'price': ArrayPrices[i],
                   'year': arrayYears[i],
                   'km': arrayKm[i],
                   'cambio': arrayCambio[i]
                   }
            arrayFinal.append(car)

        return arrayFinal
