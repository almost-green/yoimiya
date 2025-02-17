import pandas as pd
import  numpy as np
from io import  StringIO
csv_data='''
A,B,C,D,E
2,3,4,5,
6,34,6,
10,,11,8,
,,,
3,,3,,
,5,,,
'''
drop=pd.read_csv(StringIO(csv_data))
print(drop)
print('沿著row進行刪除，只要有遺失值就刪除')
drop1=drop.dropna(axis=0)
print(drop1)
print('沿著column進行刪除，只要有遺失值就刪除')
drop2=drop.dropna(axis=1)
print(drop2)
drop3=drop.dropna(axis=0,how='all')
print(drop3)