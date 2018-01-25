# import out libraries to scrape what we want
import bs4 as bs
import time
import re
from datetime import date
from urllib.request import Request, urlopen

# we cannot just use our normal bs4 impl. we need to give the
# mod_security server feature that mlh.io has a known user agent
# like mozilla.
location = input("Enter a location for a hackathon: ")
sauce = Request('https://mlh.io/seasons/na-2018/events',
headers={'User-Agent': 'Mozilla/5.0'})
req = urlopen(sauce).read()
soup = bs.BeautifulSoup(req, 'lxml')

for span in soup.find_all('span'):
    if span.find(text=re.compile(location)):
        for text in span:
            print(text)
