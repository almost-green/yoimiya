import  pandas as pd
data={'Name':['Tom','Jack','Steve','Ricky'],
      'Age':[28,34,29,42]}
print(data.__class__)
print(data)
df=pd.DataFrame(data)
print(df)
df2=pd.DataFrame(data,index=['man1','man2','man3','man4'])
print(df2)
