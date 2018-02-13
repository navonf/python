from bs4 import BeautifulSoup
import requests

# Okay, I **WANT** to say all the python libraries, we will use pip (or pip3)
# to install them. For Mac, we're using pip3 because Mac has 2 versions of
# python usually.. 2.7 & 3.6.
#
# Run the command below in terminal:
# pip3 install requests beautifulsoup4 lxml
#
# If you get the need permission needed/red text, just put 'sudo' in front
# of the command above, no quotes.
#
# This **should** be all the python libraries we need. As you can tell, this
# implementation has less imports (line 1 & 2) so hopefully we won't run into
# any 'urlopen' or 'SSL certificate' errors.

# Request
# It's a bit different than bs.py, but we use requests.get(url) instead of Request(url)
kind = input("Enter a type of beer [sour, ipa, ale]: ")
url = 'https://www.beeradvocate.com/search/?q='
url = url + kind
r  = requests.get(url)
data = r.text

# Parse
soup = BeautifulSoup(data, 'lxml')
elements = soup.find_all('b')

# Pretty
del elements[:4]
for i in range(0, len(elements)):
    string = str(elements[i])
    string = string[3:]
    string = string[:-4]
    print(string)
