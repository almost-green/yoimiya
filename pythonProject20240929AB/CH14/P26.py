import pandas as pd
from  datetime import  date
import  numpy as np
se2=pd.read_csv(
    'se2.csv',
    names=['Date','num'])
print('顯示索引1')
print(se2.index)
print('顯示資料類型1')
print(se2.dtypes)
print(se2)
se2['Date']=pd.to_datetime(se2['Date'])
print('顯示資料類型2')
print(se2.dtypes)
se2.set_index('Date',inplace=True)
print('顯示索引2')
print(se2.index)
print(se2)
print('計算每個月資料總和')
se2M=se2.resample('M').sum()
print(se2M)
