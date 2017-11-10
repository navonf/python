# Python practice
# This script pulls BABA, MOMO, and AMZN current stock prices, feel free to add.

import bs4 as bs
import urllib.request

# grab the sauce bois, and read it
sauce = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/baba/').read()

# pass the HTML code to BeautifulSoup
soup = bs.BeautifulSoup(sauce, 'lxml')
baba = float(soup.td.string)
flux = list(soup.find('td', attrs={'class': 'value-change'}).string)
net_change = ""
i = 0

while flux[i] != ' ':
    net_change += flux[i]
    i += 1;

print("Current price of BABA:   ", baba)
print("Yeserday's price of BABA:", baba + float(net_change))
print("Change since yesterday:  ", soup.find('td', attrs={'class': 'value-change'}).string)


# grab the sauce bois, and read it
sauce2 = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/momo/').read()

# pass the HTML code to BeautifulSoup
soup2 = bs.BeautifulSoup(sauce2, 'lxml')

print("Current price of MOMO:    " + soup2.td.string)

# grab the sauce bois, and read it
sauce3 = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/AMZN/').read()

# pass the HTML code to BeautifulSoup
soup3 = bs.BeautifulSoup(sauce3, 'lxml')

print("Current price of AMZN:    " + soup3.td.string)
