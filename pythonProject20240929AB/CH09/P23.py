#Windows環境的語法
from os import listdir
from os.path import isfile, isdir, join
import os
sysDrv = os.environ["HOMEDRIVE"]
userHomeDrv = os.environ["HOMEPATH"]
#mypath = "C:/Users/gjun/Documents"
mypath = sysDrv+userHomeDrv+"/Documents"
files = listdir(mypath)
for f in files:
  fullpath = join(mypath, f)
  if isfile(fullpath):
    print("檔案：", f)
  elif isdir(fullpath):
    print("目錄：", f)

