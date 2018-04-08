import requests
from xml.etree import ElementTree

def getHeadlines():
    arg = 'NKE'
    url = "http://finance.yahoo.com/rss/headline?s="+arg
    response = requests.get(url)
    tree = ElementTree.fromstring(response.content)
    headlines = []
    for i in tree.iter('item'):
        for c in i:
            if c.tag == 'title':
                headlines.append(c.text)
    return headlines

def showHeadlines(h):
    l = len(h)
    for i in range(0,l):
        print i, h[i]

def main ():
    h = getHeadlines()
    print "Now Showing all headlines for NKE"
    showHeadlines(h)
    print "\n\n"
    num = raw_input("Enter the line number of the headline you want  :")
    print h[int(num)]

if __name__== "__main__":
    main()
