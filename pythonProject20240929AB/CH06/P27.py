#傳統函數
def f1(x):
  return x**2
def f2(x):
  return x**3
def f3(x):
  return x**4
list1=[f1,f2,f3]
for f in list1:
  print(f(3))
#匿名函數
list2=[
    lambda x:x**2,
    lambda x:x**3,
    lambda x:x**4
]
for g in list2:
  print(g(3))
