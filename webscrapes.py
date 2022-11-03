from bs4 import BeautifulSoup
import requests
url="https://getpython.wordpress.com/"
source=requests.get(url)
soup=BeautifulSoup(source.text,'html')
title=soup.find('title')
print("this is with html tags :",title)
qwery=soup.find('h1')
print("this is without html tags:",qwery.text)
links=soup.find('a')
print("Here i can my links",links)
