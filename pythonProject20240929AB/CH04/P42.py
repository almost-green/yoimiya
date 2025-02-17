list1=[1,'x',2,'x',3]
list1.remove('x')
print(list1)
list1.remove('x')
print(list1)
if 'x' in list1:
  print('x在list1內')
  list1.remove('x')
  print(list1)
else:
  print('no data')
