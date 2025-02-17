import numpy as np
a=np.array([
  [4,-7],
  [2,-3]
]
)
a_inv=np.linalg.inv(a)
print(a_inv)
print()
print(a.dot(a_inv))
