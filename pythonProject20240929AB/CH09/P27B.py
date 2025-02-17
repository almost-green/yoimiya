#Windows環境的語法
from os import walk
import os
sysDrv = os.environ["HOMEDRIVE"]
userHomeDrv = os.environ["HOMEPATH"]
mypath = sysDrv+userHomeDrv+"/Downloads"
for root, dirs, files in walk(mypath):
  #print("路徑：", root)
  #print("  目錄：", dirs)
  #print("  檔案：", files)
  for file in files:
      ext = str(file).split(".")[-1].lower()
      if ext=='png' or ext=='gif' or ext=='mbp':
          print("圖檔:", os.path.join(root, file))
