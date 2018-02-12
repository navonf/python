# This script pulls BABA, MOMO, and BST current stock prices, feel free to add.
# 2 baba @ 153.57 = 307.14
# 8 momo @ 40.64 = 325.12
# 4 BST @ 26.42 = 105.68
import bs4 as bs
import urllib.request
import numpy as np

# my current stocks
babaInvested = [153.57, 153.57]
momoInvested = [40.64, 40.64, 40.64, 40.64, 40.64, 40.64, 40.64, 40.64]
bstInvested = [26.42, 26.42, 26.42, 26.42]

totalInvested = sum(babaInvested) + sum(momoInvested) + sum(bstInvested)
print("Current amount invested:", totalInvested)

# grab the sauce bois, and read it
sauce = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/baba/').read()

# pass the HTML code to BeautifulSoup
soup = bs.BeautifulSoup(sauce, 'lxml')
baba = float(soup.td.string)
print("Current price of BABA:  ", baba)

# grab the sauce bois, and read it
sauce2 = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/momo/').read()

# pass the HTML code to BeautifulSoup
soup2 = bs.BeautifulSoup(sauce2, 'lxml')
momo = float(soup2.td.string)
print("Current price of MOMO:   "     + soup2.td.string)

# grab the sauce bois, and read it
sauce3 = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/BST/').read()

# pass the HTML code to BeautifulSoup
soup3 = bs.BeautifulSoup(sauce3, 'lxml')
bst = float(soup3.td.string)
print("Current price of BST:    " + soup3.td.string)

totalMade = (baba * len(babaInvested)) + (momo * len(momoInvested)) + (bst * len(bstInvested))
t = totalMade - totalInvested
t = round(t, 2)

if totalMade > totalInvested:
    print("Current amount made:    ", str(t))
else:
    print("lol")
