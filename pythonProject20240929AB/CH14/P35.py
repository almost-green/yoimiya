import pandas  as pd
import numpy as np
df=pd.read_csv('2017.csv',encoding='utf-8-sig')
print(df)
print('將資料轉換為html，以便查看')
html=df.to_html()
with open('work1.html','w',encoding='utf-8') as file:
    file.writelines('<meta charset="utf-8">\n')
    file.write(html)
df=df.replace('—',np.nan)
df=df.replace('…',np.nan)
html=df.to_html()
with open('work2.html','w',encoding='utf-8') as file:
    file.writelines('<meta charset="utf-8">\n')
    file.write(html)