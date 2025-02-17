import pandas as pd
auto_price=pd.read_csv('Automobile.csv')
print(auto_price.head())
print('轉換為網頁，了解所有資料')
auto_price.to_html('auto1.html')
print('了解欄位名稱，-容易有被誤判的風險')
print(auto_price.columns)
print('儲存欄位名稱')
cols=auto_price.columns
auto_price.columns=[str.replace('-','_') for str in cols]
print(auto_price.columns)
print('查看資料內是否有遺失值')
print(auto_price.isnull().any())
print('查看每個欄位的資料型態')
print(auto_price.dtypes)
print('price欄位應該是數值資料型態，怎會是object型態？')
print(auto_price['price'])
import numpy as np
print('查看哪些欄位有？')
list1=[]
for col in auto_price:
  for filed1 in auto_price[col]:
    if filed1=='?':
      list1.append(col)
print(list1)
print(len(list1))
print('太多資料重複，希望資料不要重複出現，我們將資料轉換為set型態')
set1=set(list1)
print(set1)
print(len(set1))
list2=list(set1)
for column in list2:
  auto_price.loc[auto_price[column]=='?',column]=np.nan
auto_price.to_csv('auto1a.csv')
auto_price.to_html('auto1a.html')
print('查看資料內是否有遺失值')
print(auto_price.isnull().any())
print('查看每個欄位的資料型態')
print(auto_price.dtypes)
print('刪除之前資料的形狀')
print(auto_price.shape)
print(auto_price.isnull( ).sum( ))
print('normalized_losses欄位的遺失值太高，共有41個，所以捨棄這個欄位')
try:
  auto_price.drop(['normalized_losses'],axis=1,inplace=True)
except:
  pass
print('刪除normalized_losses欄位的形狀')
print(auto_price.shape)
print('6個欄位有18個遺失值，代表有些欄位的遺失值數量很多')
print(auto_price.isnull( ).sum( ))
print('欄位內有2個或4個遺失值，那可以接受')
auto_price.dropna(axis=0,inplace=True)
print('dropna後的形狀')
print(auto_price.shape)
list3=[]
for i in auto_price.columns:
  print('欄位名稱：',i)
  print('欄位資料型態：',auto_price[i].dtype)
  if auto_price[i].dtype==object:
    try:
       print('進行轉換')
       auto_price[i]=auto_price[i].astype('float')
       list3.append(i)
    except:
      pass
print('哪些欄位轉換為float')
print(list3)
print('描述數值型態資料')
print(auto_price.describe( ))
print('描述字串型態資料')
print(auto_price.describe(include=['object']))
print('分別挑選出數值型態與字串型態欄位')
cols4=[]#字串
cols5=[]#數值
for i in auto_price.columns:
  if auto_price[i].dtype==object:
    cols4.append(i)
  else:
    cols5.append(i)
print('數值欄位有：\n',cols4)
print('字串欄位有：\n',cols5)
print('字串型資料內資料出現的筆數統計')
for column in cols4:
  print('欄位為：',column)
  print(auto_price[column].value_counts( ))
  print( )
print('字串資料以長條圖顯示')
import matplotlib.pyplot as plt
for cols in cols4:
  auto_price[cols].value_counts( ).plot(
      kind='bar',title=cols,rot=45
  )
  plt.show( )
print('數值資料以直方圖顯示')
import matplotlib.pyplot as plt
for cols in cols5:
  auto_price[cols].plot(
      kind='hist',title=cols,rot=45
  )
  plt.show( )
print('數值資料與price之間關係，以散佈圖顯示')
for cols in cols5:
  auto_price.plot(
      kind='scatter',
      title=cols,x=cols,y='price',rot=45
  )
  plt.show( )
print('想要了解多個欄位之間的關係')
import seaborn as sns
sns.heatmap(auto_price[cols5].corr( ))
plt.show( )
