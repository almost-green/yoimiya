import numpy as np
B = np.array([
    [8, 2],
    [12, 3]
])
try:
  B_inv = np.linalg.inv(B)
except np.linalg.LinAlgError:
  print('矩陣 B 是不可逆矩陣')
