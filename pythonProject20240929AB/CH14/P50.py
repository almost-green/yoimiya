import pandas as pd
import  numpy as np
from io import  StringIO
csv_data='''
A,B,C,D
2,3,5,5
5,5,5,5
5,5,5,5
13,23,5,5
'''
df2=pd.read_csv(StringIO(csv_data))
print(df2)
print("-------0---------")
print(df2.duplicated())
print("-------1---------")
print(df2.duplicated('A'))
print("-------2---------")
print(df2.duplicated('D'))
print("-------3---------")
