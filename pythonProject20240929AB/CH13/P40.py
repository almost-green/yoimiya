import  pandas as pd
import  numpy as np
df=pd.DataFrame(
    np.arange(48).reshape(6,8),
    index=['a','b','c','d','e','f'],
    columns=['s','t','u','v','w','x','y','z'])
print(df)
# print()
# print(df.iloc[1,:])
# print('1---')
# print(df.iloc[2,4])
# print('2---')
print(df.iloc[[2,4],[4,6]])
print('3---')
print(df.iloc[2:4,4:6])
print('4---')
print(df.iloc[:,-3])
print('5---')