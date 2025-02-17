from rembg import remove
from os import walk
import os
originalPath = "C:/Users/User/Desktop/original pic"
for root, dirs, files in walk(originalPath):
  for file in files:
      ext = str(file).split(".")[-1].lower()
      if ext=='jpeg' or ext == "jpg" or ext == "png" or ext == "jfif":
          fullFileName = os.path.join(root, file).replace('\\','/')
          print("圖檔:", fullFileName)
          try:
              with open(fullFileName, "rb") as i, open(fullFileName+'.png', 'wb') as o:
                  input = i.read()
                  output = remove(input)
                  o.write(output)
                  print("成功去背:",fullFileName)
          except:
              print('轉檔失敗:',fullFileName)
