import requests
from Keys import line_notify_key
url='https://notify-api.line.me/api/notify'
print('請留意token是你的不是老師的')
token=line_notify_key
headers={'Authorization':'Bearer '+token}
data={
    'message':'那麼棒',
    'stickerPackageId':'8525',
    'stickerId':'16581302'
}
data=requests.post(url,headers=headers,data=data)
print(data)