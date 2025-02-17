import numpy as np
a = np.array( [6, 7, 8, 9] )
b = np.arange(4)
c = a - b
print("a=>",a)
print("b=>",b)
print("c=>",c)
d = b**2
print("d=>",d)
f = np.array([5, -1, 3, 9, 0])
print("f=>",f)
f[f<=3] = 1
print("f=>",f)
