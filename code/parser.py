import bs4 as bs
from urllib.request import Request, urlopen

sauce = Request('https://www.beeradvocate.com/beer/', headers={'User-Agent': 'Mozilla/5.0'})
req = urlopen(sauce).read()
soup = bs.BeautifulSoup(req, 'lxml')

print(soup)
