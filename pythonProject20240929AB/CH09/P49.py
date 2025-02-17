import shutil
import os
try:
  os.mkdir('test2')
  print('建立目錄')
except:
  print('建立目錄失敗')
input('請按任何鍵繼續')
with open('./test2/test2.txt', 'a') as file2:
  file2.write('Programming is Fun.')
  file2.write('Programiz for beginners')
  print('完成附加檔案')
input('請按任何鍵繼續')
print('查看目錄內容')
print(os.listdir('./test2'))
input('請按任何鍵繼續')
try:
  shutil.rmtree("test2")
  print('刪除test2目錄')
except:
  print('刪除目錄失敗')
