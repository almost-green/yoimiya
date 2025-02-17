import matplotlib.font_manager as fm
path = 'NotoSerifCJKtc-Medium.otf'
fontprop = fm.FontProperties(fname=path, size=13)
import  matplotlib.pyplot as plt
import  numpy as np
plt.figure(figsize=(8,5))
x=np.linspace(-10,10,50)
y1=2*x+1
y2=x**2-3*x-11
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='dashdot')
plt.grid()
plt.title('中文',fontproperties=fontprop)
plt.xlabel('水平x',fontproperties=fontprop,labelpad=15)
plt.ylabel('垂直y',fontproperties=fontprop,rotation=0,labelpad=15)
plt.show()
