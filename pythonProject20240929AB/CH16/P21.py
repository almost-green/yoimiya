import pandas as pd
import numpy as np
fortune = pd.read_csv("fortune1000.csv",index_col='Rank')
print(fortune)
a=fortune['Revenue']
b=fortune['Employees']
print('共變異數的推算，計算波動的程度')
print(np.cov(b,a))
print('相關係數的推算，計算兩者的相關性')
print(np.corrcoef(a,b))
