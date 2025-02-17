import  matplotlib.pyplot as plt
import  numpy as np
x=np.linspace(10,50,50)
y1=-np.power(x,2)+30*x-11
y2=np.power(x,2)-3*x-11
plt.plot(x,y2,linewidth=0.5,linestyle='--')
plt.plot(x,y1,color='red',linewidth=3.0,linestyle=':')
plt.axvline(30,0.8,0.5,color='blue')
plt.axhline(500,0.8,0.5,color='red')
plt.title('Title標題')
plt.xlabel('xlabel水平')
plt.ylabel('ylabel垂直')
plt.show()
