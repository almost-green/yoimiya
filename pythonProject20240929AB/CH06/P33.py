#假設list內容有空白這個資料，請將空白資料轉為0
list3=[1,2,3,'',4,5,'',6]
print(len(list3))
print('匿名函數+map')
list6=map(lambda x:x if x!='' else 0,list3)
print(list(list6))
print('匿名函數+filter')
list7=filter(lambda x:x!='',list3)
print(list(list7))

