#假設list內容有空白這個資料，請將空白資料轉為0
list3=[1,2,3,'',4,5,'',6]
print(len(list3))
print('傳統程式')
list4=[ ]
for x in list3:
  if x!='':
    list4.append(x)
  else:
    list4.append(0)
print(list4)
print('匿名函數')
list6=map(lambda x:x if x!='' else 0,list3)
print(list(list6))
