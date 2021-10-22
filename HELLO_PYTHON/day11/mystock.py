from bs4 import BeautifulSoup
import requests
from _datetime import datetime
from day11.dao_stock import DaoStock
from time import sleep

ds = DaoStock()

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

for i in range(10):
    response = requests.get(url)
    g_time = datetime.today().strftime('%Y%m%d.%H%M')
    # 20211015.1013
    response.encoding='EUC-KR'

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    st2s = soup.select(".st2")
    for idx, st2 in enumerate(st2s):
        s_name = st2.text
        s_code = st2.a['title']
        price = st2.parent.select('td')[1].text.replace(",","")
        ds.myinsert(s_code, s_name, price, g_time)
        #print(idx, st2.parent.select('td')[1].text.replace(",",""))
    ds.mycommit()
    sleep(60)
    
# ================= DB 추가부분======================



# tables = soup.select('table')
# trs = tables[0].select('tr')
#
# for idx, tr in enumerate(trs):
#     if idx > 0:
#         tds = tr.select('td')
#         print(tds[1].text, tds[2].text, tds[3].text)

#data = soup.select('td')

#print(data)