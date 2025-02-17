import  pandas as pd
import  numpy as np
df=pd.DataFrame(
    np.arange(48).reshape(6,8),
    index=['a','b','c','d','e','f'],
    columns=['s','t','u','v','w','x','y','z']
)
print(df)
print()
print(df.iloc[1::2,1:7:2])
print('---1---')
print(df.loc['b'::2,'t':'y':2])
print('---2---')