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
df.to_html('df1.html')
df.to_csv('df1a.csv')
df.to_csv('df1b.csv',index=False)