set1={3,1,2,3,4,'set1',5.5}
print(set1)
adddata='Hello'
set1.add(adddata)
print(set1)
set1.add(30)
print(set1)
set1.remove('set1')
print(set1)
print('以下為有問題的語法')
#print(set1[1]) #set沒有索引值，所以不能指定索引值
#set1[2]='A'
print('我要撈資料與資料變更')
list1=list(set1)
print(list1)
print(list1[1])
list1[2]='A'
print(list1)
