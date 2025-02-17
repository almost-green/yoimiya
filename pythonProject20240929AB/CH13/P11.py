import  pandas as pd
fruits=['蘋果','橘子','梨子','櫻桃']
quantities=[15,33,45,55]
import  numpy as np
n1=np.array(quantities)
s1=pd.Series(quantities)
s2=pd.Series(quantities,index=fruits)
print(n1);print('-'*70)
print(s1);print('-'*70)
print('s1 index:',s1.index)
print('-'*70)
print('s1 values:',s1.values)
print('-'*70)
print(s2);print('-'*70)
print('s2 index:',s2.index)
print('-'*70)
print('s2 values:',s2.values)
print('-'*70)
print('s2的第二筆資料取值')
print(s2[1])
print(s2['橘子'])