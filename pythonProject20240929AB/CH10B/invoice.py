import requests
from bs4 import BeautifulSoup
url = 'https://invoice.etax.nat.gov.tw/index.html'
r= requests.get(url)
r.encoding = 'UTF-8'
sp = BeautifulSoup(r.text, 'html.parser')
datas = sp.select('.etw-on')
print('開獎月份:',datas[0].text)
datas = sp.select('.etw-tbiggest')
result = datas[0].find('span')
print('特別號:',result.text)
result = datas[1].find('span')
print('特獎:',result.text)
datas = sp.select('.mb-md-4')
for i in range(3):
    temp = datas[i].select('.font-weight-bold')
    print('頭獎:',temp[0].text+temp[1].text)
