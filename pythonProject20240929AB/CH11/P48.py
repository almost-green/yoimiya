import numpy as np
x = np.loadtxt('data1.csv',
               skiprows=1,
               delimiter=',')
print(x)
y, z = np.loadtxt('data1.csv'
                  ,skiprows=1,
                  unpack=True,
                  delimiter=',')
print("Value1=",y)
print("Value2=",z)
