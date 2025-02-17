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
print(df2.drop_duplicates(keep='last'))
print("-------1---------")
print(df2.drop_duplicates(keep=False))
print("-------2---------")
print(df2.drop_duplicates(subset=['C','D']))
print("-------3---------")
print(df2.drop_duplicates(subset=['C','D'],keep='last'))
print("-------4---------")
print(df2.drop_duplicates(subset=['C','D'],keep=False))
print("-------5---------")
print(df2.drop_duplicates(subset=['A','D'],keep=False))
print("-------6---------")
print(df2.drop_duplicates(subset=['B']))
print("-------7---------")
