import numpy as np
from numpy import genfromtxt
a = np.genfromtxt('data3b.csv',
                  dtype='int',
                  delimiter=',',
                  skip_header=1,
                  encoding='utf-8-sig',
                  unpack=True)
x=np.size(a, axis=0)
print(x)
print(a.shape)
print(a)
print(a[0,0])
print(a[1,0])
print(a[2,0])
