import os
try:
  os.remove("test2.txt")
  print('檔案已經刪除')
except:
  print('檔案刪除異常')
import os
try:
  os.rmdir("new_one")
  print('空目錄已經刪除')
except:
  print('空目錄刪除異常')
