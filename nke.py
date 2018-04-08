import requests
from xml.etree import ElementTree

def get_res():
    arg = 'NKE'
    url = "http://finance.yahoo.com/rss/headline?s="+arg
    response = requests.get(url)
    tree = ElementTree.fromstring(response.content)
    return tree

def getHeadlines(tree):
    headlines = []
    for i in tree.iter('item'):
        for c in i:
            if c.tag == 'title':
                headlines.append(c.text)
    return headlines
def getDescription(tree):
        description = []
        for i in tree.iter('item'):
            for c in i:
                if c.tag == 'description':
                    description.append(c.text)
        return description

def showHeadlines(h):
    l = len(h)
    for i in range(0,l):
        print i, h[i]

def main ():
    tree = get_res()
    h = getHeadlines(tree)
    d = getDescription(tree)
    print "Now Showing all headlines for NKE"
    showHeadlines(h)
    print "\n\n"
    num = raw_input("Enter the line number of the headline you want  :")
    print h[int(num)]
    print d[int(num)]

if __name__== "__main__":
    main()
