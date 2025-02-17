import numpy as np
print('總金額 除以 單價')
print('總金額 乘以 單價的反矩陣')
print('得到反矩陣代表可以被整除')
price1=np.array([[3,3.5],[3.2,3.6]])
total=[[118.4,135.2]]
try:
  price1_inv=np.linalg.inv(price1)
  print(price1_inv)
  print(np.dot(total,price1_inv))
except:
  print('得不到反矩陣')