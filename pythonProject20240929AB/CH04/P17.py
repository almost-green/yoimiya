a=(3,1,2,3,4,'set1',5.5)
print(a)
#b=a+5
#b=a+(5) #() 被認為是小括弧，5不會被當作tuple資料
b=a+(5,)
print(b)
b=b+('15',)
print(b)
print(b[1])
#b[2]='A' #沒有支援這種語法
print(b)
#b[2]=('A',) #沒有支援這種語法
print(b)
