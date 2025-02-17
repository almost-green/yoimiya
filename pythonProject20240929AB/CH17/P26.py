import pandas as pd
tvmarketing=pd.read_csv('tvmarketing.csv')
print(tvmarketing.head())
print(tvmarketing.shape)
tvmarketing.to_html('tvmarketing1.html')
print(tvmarketing.isnull().any())
print(tvmarketing.dtypes)
import matplotlib.pyplot as plt
plt.scatter(tvmarketing['TV'],tvmarketing['Sales'])
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show()
print('我們先建立X與y資料，後續才能進行切割')
X=tvmarketing['TV']
y=tvmarketing['Sales']
print('準備做資料切割')
from sklearn.model_selection import train_test_split
import sklearn.linear_model
X_train,X_test,y_train,y_test=train_test_split(X,
                                               y,
                                               test_size=0.3)
print(X_train.shape)
print(X_test.shape)
model=sklearn.linear_model.LinearRegression()
import numpy as np
X_train=np.array(X_train).reshape(-1,1)
print(X_train.shape)
model.fit(X_train,y_train)
print('迴歸係數：',model.coef_)
print('截距：',model.intercept_)
import matplotlib.pyplot as plt
X2=np.array(X).reshape(1,-1)
y2=(model.coef_)*X2+model.intercept_
plt.scatter(X2,y)
plt.scatter(X2,y2,c='red')
plt.show()
print('進行預估')
print('我們預估X_test 預估測試的資料 預估之後會產生結果')
print('例如y_pred')
print('我們拿預估之後的結果y_pred與y_test測試的目標來做比較')
print('比較預估結果與真實結果是否相同')
X_test=np.array(X_test).reshape(-1,1)
y_pred=model.predict(X_test)
print(y_pred)
print('正確結果如下')
print(y_test)