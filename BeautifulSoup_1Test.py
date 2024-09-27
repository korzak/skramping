from urllib.request import urlopen
from bs4 import BeautifulSoup
URL1 ="http://www.pythonscraping.com/pages/page1.html"

HTML2 = urlopen(URL1)
# bs = BeautifulSoup(HTML2.read(), 'html.parser')
# bs = BeautifulSoup(HTML2.read(),'lxml') # parser  lxml pip3 install lxml
bs = BeautifulSoup(HTML2.read(),'html5lib') # parse html5lib pip3 install html5lib
print(bs.h1)
