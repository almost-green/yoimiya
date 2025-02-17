from Keys import line_notify_key
import requests
url='https://notify-api.line.me/api/notify'
print('請留意token是你的不是老師的')
radar_url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON'
radar = requests.get(radar_url)
json1=radar.json()
print(json1)
print('擷取氣象雷達圖')
img1=json1['cwaopendata']['dataset']['resource']['ProductURL']
time1=json1['cwaopendata']['dataset']['DateTime']
headers={'Authorization':'Bearer '+line_notify_key}
data={
    'message':time1+'氣象雷達圖',
    'imageThumbnail':img1,
    'imageFullsize':img1
}
data=requests.post(url,headers=headers,data=data)
print(data)