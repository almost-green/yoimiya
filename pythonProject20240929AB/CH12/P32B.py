# import matplotlib.font_manager as fm
# path = 'NotoSerifCJKtc-Medium.otf'
# fontprop = fm.FontProperties(fname=path, size=13)
import  matplotlib.pyplot as plt
import  numpy as np
plt.figure(figsize=(8,5))
# 修正中文亂碼
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
x=np.linspace(-10,10,50)
y1=2*x+1
y2=x**2-3*x-11
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='dashdot')
plt.grid()
plt.title('中文',x=0.8,y=1.05)
plt.xlabel('水平x',labelpad=15)
plt.ylabel('垂直y',rotation=0,labelpad=15)
plt.show()
