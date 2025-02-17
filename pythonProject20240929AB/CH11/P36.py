import numpy as np
a = np.array([[1, 2, 3],
              [3, 6, 9],
              [2, 4, 6]])
print(a[1, 1:3])
print("---------------")
print(a[:,1])
print("---------------")
a[1, 2] = 7
print(a)
print("---------------")
a[:, 0] = [0, 9, 8]
print(a)
print("---------------")
