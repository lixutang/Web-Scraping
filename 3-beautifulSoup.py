from  urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html,"html.parser") 
for link in bsObj.find("div",{"id"""bodyCotent"}).findAll()("a",href =re.compile("^(/wiki)(?!:).)*$")):
    if 'href' in a.attrs:
        print(link.attrs['href'])
