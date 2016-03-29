 import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter -')
# url = 'http://www.azlyrics.com/lyrics/megadeth/tornadoofsouls.html'
# url = 'http://www.google.com'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve a list of anchor tags
#Each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
	print tag.get('href',None)