list2=['abc','xyz','wtu',100,2.5,3.6,5.7,50,66]
print('非Python的寫法')
list2a=[]
for x in list2:
  if isinstance(x,int):
    list2a.append(x)
print(list2a)
print('Python的寫法')
list2b=[x for x in list2 if isinstance(x,int)]
print(list2b)