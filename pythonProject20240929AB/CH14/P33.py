import pandas as pd
import  numpy as np
from io import  StringIO
csv_data='''
A,B,C,D
1.0,2.0,3.5,4
5.5,34,3.4
10,,11.5,8.5
'''
data1=pd.read_csv(StringIO(csv_data))
print(data1)
