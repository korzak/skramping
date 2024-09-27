# from urllib.request import  urlopen
# url = 'http://pythonscraping.com/pages/page1.html'
# htm = ''
# htm = urlopen(url)
# print(htm.read())

from urllib.request import urlopen

url = "http://pythonscraping.com/pages/page1.html"
response = urlopen(url)
print(response.read())
