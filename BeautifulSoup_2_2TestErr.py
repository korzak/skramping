from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def GetTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'lxml')
        Title = bsObj.body.h1
    except AttributeError as e:
        return None
    return Title

Title = GetTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if Title == None:
    print("Title could not be found")
else:
    print(Title)