from os import walk
import os
sysDrv = os.environ["HOMEDRIVE"]
userHomeDrv = os.environ["HOMEPATH"]
mypath = sysDrv+userHomeDrv+"/Documents"
for root, dirs, files in walk(mypath):
  print("路徑：", root)
  print("  目錄：", dirs)
  print("  檔案：", files)
