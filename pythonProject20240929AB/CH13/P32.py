import  pandas as pd
import  numpy as np
#龘 (音踏)  犇(音奔)
data={
    'Name':['犇','中文','龘','Ricky'],
    'Age':[28,34,29,42]
}
print(data)
df=pd.DataFrame(data)
writer=pd.ExcelWriter('df.xlsx')
df.to_excel(writer,'Sheet3')
df1=pd.DataFrame(np.arange(9).reshape(3,3),
                 index=['a','c','d'],
                 columns=['One','Two','Three'])
df1.to_excel(writer,'哈囉')
writer._save()