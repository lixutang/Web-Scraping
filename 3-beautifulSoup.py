from  urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html,"html.parser") 
for link in bsObj.findAll("a"):
    if 'href' in a.attrs:
        print(link.attrs['href'])
