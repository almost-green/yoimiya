print('假設不知道list內的資料是不適都是字串')
list2=['abc','xyz','wtu',100,2.5,3.6,5.7,50,66,'200','3.5','4.7','0.0','0','77']
list2a=[ ] #最終的字串資料
list2b=[ ] #int資料
list2c=[ ] #float資料
list2d=[ ] #混和float與str
list2e=[ ] #第一次取出的字串資料
print('取出字串部分')
list2e=[x for x in list2 if isinstance(x,str)]
print(list2e)
print('取出整數部分')
list2b=[x for x in list2 if isinstance(x,int)]
print(list2b)
print('取出浮點數部分')
list2c=[x for x in list2 if isinstance(x,float)]
print(list2c)
#挑選過後再針對字串部分，進行int( )與float()轉換。
for x in list2e:
  try:
    x2=int(x)
    print(x,'是整數資料')
    list2b.append(x2)
  except:
    list2d.append(x)
print('list2d內容')
print(list2d)
for x in list2d:
  try:
    x2=float(x)
    print(x,'是浮點數資料')
    list2c.append(x2)
  except:
    list2a.append(x)
print('取出字串部分')
print(list2a)
print('取出整數部分')
print(list2b)
print('取出浮點數部分')
print(list2c)
