import pandas as pd
from  datetime import  date
import  numpy as np
se2=pd.read_csv(
    'se2.csv',
    index_col='Date',names=['Date','num'])
print(se2.index)
print(se2.__class__)
print('顯示資料類型')
print(se2.dtypes)
print(se2)
print('計算每個月資料總和，為什麼異常?')
#se2M=se2.resample('M').sum()
#print(se2M)