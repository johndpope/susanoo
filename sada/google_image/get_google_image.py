from bs4 import BeautifulSoup
from urlparse import urlparse, parse_qs
import urllib2
import os
import sys

if not os.path.exists('output'):
    os.mkdir('output')

def download_image(url, n):
    opener = urllib2.build_opener()
    opener.addheaders = [
        ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'),
        ('Accept-Language','ja,en-us;q=0.7,en;q=0.3')
    ]
    html = opener.open(url).read()
    soup = BeautifulSoup(html, "lxml")
    elements = soup.findAll('a', attrs={'class': 'rg_l'})
    for element in elements:
        url = element['href']
        result = urlparse(url)
        queries = parse_qs(result[4])

        try:
            imgurl = queries['imgurl'][0]
            img = urllib2.urlopen(imgurl)

            content_type = img.info()['Content-type']
            extname = ''

            if content_type == 'image/jpeg':
                extname = '.jpg'
            elif content_type == 'image/png' or content_type == 'image/x-png':
                extname = '.png'
            elif content_type == 'image/gif':
                extname = '.gif'

            f = open('output/' + str(n).zfill(4) + extname, 'wb')
            f.write(img.read())
            f.close()
            n += 1
        except Exception as e:
            print e
    return n

q = sys.argv[1]
queries = [
  ['', ''],
  ['ijn=2', 'start=200'],
  ['ijn=3', 'start=300'],
  ['ijn=4', 'start=400'],
  ['ijn=5', 'start=500'],
  ['ijn=6', 'start=600'],
  ['ijn=7', 'start=700'],
]
n = 1
for query in queries:
    url = 'https://www.google.co.jp/search?q=' + urllib2.quote(q) + '&sa=X&espv=2&site=webhp&biw=1446&bih=680&tbm=isch&' + query[0] + '&ei=ImDDVvmjNeTCmAWu95jIBQ&' + query[1] + '&ved=0ahUKEwj5vLCN6_zKAhVkIaYKHa47BlkQuT0IGigB&vet=10ahUKEwj5vLCN6_zKAhVkIaYKHa47BlkQuT0IGigB.ImDDVvmjNeTCmAWu95jIBQ.i'
    n = download_image(url, n)
