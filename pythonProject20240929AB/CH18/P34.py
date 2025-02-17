import requests
from pathlib import Path
import random
import datetime
from Keys import line_notify_key
print('notify第一個運用:每天不同的早安圖')
url='https://notify-api.line.me/api/notify'
token=line_notify_key
headers={'Authorization':'Bearer '+token}
print('只傳遞年月日')
today1=datetime.datetime.now()
today2=str(today1.year)+'/'+str(today1.month)+'/'+str(today1.day)
param={'message':'早安'+today2}
image1=list(Path('morning/').glob('*.jpg'))
rand_num=random.randint(0,len(image1)-1)
image2=image1[rand_num]
image={'imageFile':open(str(image2),'rb')}
data=requests.post(url,
                   headers=headers,
                   params=param,
                   files=image)
print(data)