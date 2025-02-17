import shutil
import os
try:
  os.mkdir('test2')
  print('建立目錄')
except:
  print('建立目錄失敗')
with open('./test2/test2.txt', 'a') as file2:
  file2.write('Programming is Fun.')
  print('完成附加檔案')
with open('./test2/test3.txt', 'a') as file2:
  file2.write('Programiz for beginners')
  print('完成附加檔案')
print('查看目錄內容')
print(os.listdir('./test2'))

import zipfile
import os
def create_zip(path):
  zf = zipfile.ZipFile('{}.zip'.format(path), 'w', zipfile.ZIP_DEFLATED)
  for root, dirs, files in os.walk(path):
    for file_name in files:
      zf.write(os.path.join(root, file_name))
def ziplist(file_path):
  zf = zipfile.ZipFile(file_path, 'r')
  print(zf.namelist())
def extra_zip(file_path):
  zf = zipfile.ZipFile(file_path, 'r')
  zf.extractall()
input('請按任何鍵繼續')
try:
  print('壓縮資料')
  create_zip('test2')
except:
  print('壓縮失敗')
input('請按任何鍵繼續')
try:
  print('查看壓縮資料')
  ziplist('test2.zip')
except:
  print('查看壓縮資料失敗')
input('請按任何鍵繼續')
try:
  print('刪除目錄')
  shutil.rmtree("test2")
except:
  print('刪除目錄失敗')
input('請按任何鍵繼續')
try:
  print('解壓縮資料')
  extra_zip('test2.zip')
except:
  print('解壓縮失敗')