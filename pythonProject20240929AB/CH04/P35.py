list1=['a','b','c',1,2.5]
list1.insert(1,'x')#正數從左到右做索引值計算
print(list1)
list1=['a','b','c',1,2.5]
list1.insert(15,'x')#索引值不存在，改為最後append
print(list1)
list1.insert(-3,'y') #負數從右到左做索引值計算
print(list1)
list1.insert(-16,'z')#索引值不存在，改為最前面append
print(list1)
