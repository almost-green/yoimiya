import pandas as pd
data=['Tom','Jack','Steve','Ricky']
print(data.__class__)
print(data)
df=pd.DataFrame(data)
print(df)
df2=pd.DataFrame(data,index=['man1','man2','man3','man4'],columns=['Name'])
print(df2)
