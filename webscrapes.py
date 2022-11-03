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

#To find many links in webpage by using websoup

many_link=soup.find_all('a') 
total_links=len(many_link) 
print("total links in my website :",total_links)
print()
for i in many_link[:6]: 
    print(i)
    
#find html tags with classes

ww2_contents=soup.find_all("div",class_='toc')
for i in ww2_contents:
    print(i.text)
