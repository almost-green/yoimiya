import  pandas as pd
import  numpy as np
df=pd.DataFrame(
    np.arange(48).reshape(6,8),
    index=['a','b','c','d','e','f'],
    columns=['s','t','u','v','w','x','y','z'])
print(df)
print()
print(df.loc['b',:])
print('1---')
print(df.loc['c','w'])
print('2---')
print(df.loc[['c','e'],['w','y']])
print('3---')
print(df.loc['c':'e','w':'y'])
print('4---')
print(df.loc[:,'x'])
print('5---')