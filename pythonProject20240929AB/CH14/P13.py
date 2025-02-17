import  pandas as pd
data_url='http://bit.ly/2cLzoxH'
gap1=pd.read_csv(data_url)
print(gap1)
gap1.to_html('gap1.html')
print('總共有多少筆資料')
print(gap1.count())
print('想要查詢1997與2007年資料')
is2020=gap1['year'].isin([1997,2007])
print(is2020.head())
print(is2020.__class__)
data2020=gap1[is2020]
print(data2020)
data2020.to_html('data1997_2007.html')