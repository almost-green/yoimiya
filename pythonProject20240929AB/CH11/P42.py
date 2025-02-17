import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.resize(a, (3,3))
print(b)
print(b.shape)
print( )
b = np.resize(a, (4,4))
print(b)
print(b.shape)
