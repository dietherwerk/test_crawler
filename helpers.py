# Framework imports
import requests
import bs4


def extract_data(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)

    #setting arrays
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

    #create de dict
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
