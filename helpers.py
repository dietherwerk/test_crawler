# Framework imports
import requests
import bs4


def extract_data(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)

    #setting arrays
    arrayTitles = []
    arraySubtitles = []
    arrayPhotos = []
    arrayLinks = []
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
    for link in links:
        arrayLinks.append(link.get('href'))

    # Titles
    titles = soup.select('div#anuncios .tipo1 .info .make-model')
    for title in titles:
        arrayTitles.append(title.get_text())

    # Subtitles
    subtitles = soup.select('div#anuncios .tipo1 .info .version')
    for subtitle in subtitles:
        arraySubtitles.append(subtitle.get_text())

    # Photos
    photos = soup.select('div#anuncios .c-after .photo img')

    for photo in photos:
        arrayPhotos.append(photo.get('data-original'))

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
