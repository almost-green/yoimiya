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
drop4=drop.dropna(thresh=3)
print(drop4)
drop5=drop.dropna(subset=['C','D'])
print(drop5)
drop.dropna(thresh=2,inplace=True)
print(drop)