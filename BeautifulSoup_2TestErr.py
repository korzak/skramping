from urllib.request import urlopen
from urllib.error import HTTPError

try:
    HTML1 = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
