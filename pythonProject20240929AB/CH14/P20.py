import pandas as pd
from  datetime import  date
import  numpy as np
print('日期請調整為上課時的時間')
dates=pd.date_range('20241201',periods=200)
print(dates)
print('透過numpy產生200筆資料')
se=pd.Series(np.arange(1,201),index=dates)
print(se)
se.to_csv('se.csv')
print('計算這200筆資料總和')
se_1=se.sum()
print(se_1)
print('計算每個月資料總和')
se_2=se.resample('ME').sum()
print(se_2)
print('計算每一季資料總和')
se_3=se.resample('QE').sum()
print(se_3)