#import requests
from requests import get
#設定查詢目前IP的api網址
url = 'https://api.ipify.org'
r = get(url)
print('我目前的IP位置是:', r.text)