***Dependencies
	requests
	pprint
	bs4
	html5lib
			***

import requests
from pprint import pprint
from bs4 import BeautifulSoup
url="http://www.onefivenine.com/busRoute.dont?method=loadBusRoutesFinder"
r= requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
soup.prettify()

for link in soup.find_all('a'):
    print(link.get('href'))
