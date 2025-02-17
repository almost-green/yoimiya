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
fillmean1=fill.mean()
print(fillmean1)
print("---------------")
for x in fill:
  fill[x].fillna(fillmean1.loc[x],inplace=True)
print(fill)
print("---------------")
