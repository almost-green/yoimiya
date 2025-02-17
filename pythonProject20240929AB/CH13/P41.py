import  pandas as pd
import  numpy as np
df=pd.DataFrame(
    np.arange(48).reshape(6,8),
    index=['a','b','c','d','e','f'],
    columns=['s','t','u','v','w','x','y','z'])
print(df)
print()
print(df.iloc[2:,4:])
print('1---')
print(df.iloc[:4,:6])
print('2---')
print(df.loc['c':,'w':])
print('3---')
print(df.loc[:'e',:'y'])
print('4---')