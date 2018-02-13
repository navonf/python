import bs4 as bs
from urllib.request import Request, urlopen

# Prompted user, made request
kind = input("What type of beer? [ipa, stout, sour]: ")
url = 'https://www.beeradvocate.com/search/?q='
url = url + kind
req = Request(url)

# Parse!!
sauce = urlopen(req).read()
soup = bs.BeautifulSoup(sauce, "lxml")
elements = soup.find_all('b')

# Pretty
del elements[:4]
for i in range(0, len(elements)):
    string = str(elements[i])
    string = string[3:]
    string = string[:-4]
    print(string)
