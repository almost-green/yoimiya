dict1={'a':100,'b':200,'c':300}
print(dict1)
del dict1['c']
print(dict1)
if 'c' in dict1.keys( ):
  del dict1['c']
  print(dict1)
  print("已經刪除")
else:
  print("無法刪除")
