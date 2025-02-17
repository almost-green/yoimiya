#Windows環境的語法
import os
print('顯示目前目錄內資料清單')
print(os.listdir())
print('-'*700)

sysDrv = os.environ["HOMEDRIVE"]
userHomeDrv = os.environ["HOMEPATH"]
try:
  #print(os.listdir('/content/drive/MyDrive'))
  print(os.listdir(sysDrv+userHomeDrv+"/Downloads"))
except:
  print('無法顯示指定目錄內資料清單')

