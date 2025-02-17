list2=['abc','xyz','wtu',100,2.5,3.6,5.7,50,66]
print('挑選出字串的資料儲存至list2a')
list2a=[x for x in list2 if isinstance(x,str)]
print(list2a)
print('挑選出整數的資料儲存至list2b')
list2b=[x for x in list2 if isinstance(x,int)]
print(list2b)
print('挑選出浮點數的資料儲存至list2c')
list2c=[x for x in list2 if isinstance(x,float)]
print(list2c)
