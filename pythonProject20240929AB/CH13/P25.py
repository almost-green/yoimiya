import pandas as pd
df1 = pd.read_csv('ex1.csv')
print('輸出ex1.csv完整資訊')
print(df1)
print("-----")

df2= pd.read_csv('ex1.csv',header=None)
print('輸出ex1.csv，省略抬頭那一列')
print(df2)
print("-----")

df3= pd.read_csv('ex1.csv',names=list('abcde'))
print('輸出ex1.csv，column名稱變更')
print(df3)
print("-----")