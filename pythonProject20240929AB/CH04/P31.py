print('假設輸入0代表結束，依序輸入各種數字')
list1=[]
while True:
  try:
    a=int(input('請輸入發票金額'))
    if a!=0:
      list1.append(a)
    else:
     break
  except:
    print('請輸入整數')
print('你輸入')
print(list1)
print('請刪除重複的金額，想知道到底有那些數字')
set1=set(list1)
print(len(list1))
print(len(set1))
print(set1)
list2=list(set1)
print(list2)

