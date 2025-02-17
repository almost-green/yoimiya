import pandas as pd
import  numpy as np
from io import  StringIO
csv_data='''
A,B,C,D
1.0,2.0,x,4
5.5,34,3.4,x
10,x,11.5,8.5
'''
data3=pd.read_csv(StringIO(csv_data))
print(data3)
print(data3.count())
data3=data3.replace('x',np.nan)
print(data3)
#print(data3.mean()) #為何不能處理?
print(data3.count())
print(data3.isnull().any())
print(data3.isnull().sum())