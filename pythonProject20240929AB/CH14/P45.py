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
fill=pd.read_csv(StringIO(csv_data))
print(fill)
print("---------------")
fill_zero = fill.fillna(0)
print(fill_zero)
print("---------------")
fill_zero = fill.fillna(0,limit=2)
print(fill_zero)
print("---------------")
fill2=fill.fillna(method='pad')
print(fill2)
print("---------------")
fill3=fill.fillna(method='backfill')
print(fill3)
print("---------------")