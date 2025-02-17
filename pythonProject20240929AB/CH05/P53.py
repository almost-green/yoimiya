def manyvalue(a,b):
  c=a+b
  return(a,b,c)
print('也許一開始不知道他會回傳多個資料')
answer1=manyvalue(1,2)
print(answer1)
print(answer1.__class__)
print('可以計算回傳的數量:',len(answer1))
for x in answer1:
  print(x)

