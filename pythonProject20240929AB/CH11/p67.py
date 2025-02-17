import numpy as np
a = np.array([[1, 2, 3], [13, 6, 9], [12, 24, 36]])
print(a)
print(np.diff(a))
print("---------------")
print(np.diff(a,axis=0))
print("---------------")
print(np.diff(a,axis=1))
print("---------------")
