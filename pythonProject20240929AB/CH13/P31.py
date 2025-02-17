import  pandas as pd
import  numpy as np
#龘 (音踏)
#犇(音奔)
data={
    'Name':['犇','中文','龘','Ricky'],
    'Age':[28,34,29,42]
}
print(data)
df=pd.DataFrame(data)
print(df)
df.to_csv('df1c.csv',index=False,encoding='utf-8-sig')
df.to_csv('df1d.csv',index=True,encoding='utf-8-sig')
df.to_csv('df1e.csv',index=False,encoding='utf-8')
df.to_csv('df1f.csv',index=True,encoding='utf-8')