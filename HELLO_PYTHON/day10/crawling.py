import requests
import os
import sys
import urllib.request
import pymysql
from bs4 import BeautifulSoup
from day10.dao_sawon import DaoMovie

client_id = "uravXJxXLnQNjfRVkqKW"
client_secret = "6U3bzQbxWU"
encText = urllib.parse.quote("tenet")
#print('시작')
url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
# source = requests.get('http://127.0.0.1:9999/sawon_list').text
source = response_body.decode('utf-8')
soup = BeautifulSoup(source, 'html.parser')
soupLxml = BeautifulSoup(source, 'lxml')

items = soup.select('item')

itemsLxml = soupLxml.select('item');

items_find_all = soup.find_all('item');
#print(itemsLxml)

for item in items:
    title = item.title.text
    image = item.image.text
    subtitle = item.subtitle.text
    pubDate = item.pubdate.text
    director = item.director.text
    actor = item.actor.text
    useRating = item.userrating.text

for item in itemsLxml:
    image = item.image.text

for item in items_find_all:
    link = item.link.text
    
print(title)
print(link)
print(image)
print(subtitle)
print(pubDate)
print(director)
print(actor)
print(useRating)



# ================= DB 추가부분======================

# dm = DaoMovie()
# cnt = dm.myinsert(title, link, image, subtitle, pubDate, director, actor, useRating)
# print("cnt = ",cnt)
    

# tables = soup.select('table')
# trs = tables[0].select('tr')
#
# for idx, tr in enumerate(trs):
#     if idx > 0:
#         tds = tr.select('td')
#         print(tds[1].text, tds[2].text, tds[3].text)

#data = soup.select('td')

#print(data)