import numpy as np
from numpy import genfromtxt
a = np.genfromtxt('data2.csv',
                  delimiter=',',
                  skip_header =1)
print(a)
np.savetxt('data1a.csv',
           a, delimiter=',',
           fmt='%1.4f')
b = np.genfromtxt('data2.csv',
                  delimiter=',',
                  skip_header =1, filling_values= 0.001)
print(b)
np.savetxt('data1b.csv'
           , b,
           delimiter=',')
