import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,8)
y=[1,3,3,12,5,7,9]
plt.plot(x,y)
plt.show()
slope,intercept=np.polyfit(x,y,1) #1代表1次方
print(slope,intercept)
y1=[slope*i+intercept for i in x]
plt.plot(x,y,'--')
plt.plot(x,y1,'b')
plt.show()
slope1,slope2,intercept=np.polyfit(x,y,2) #2代表2次方
print(slope1,slope2,intercept)
y1=[slope1*i**2+slope2*i+intercept for i in x]
plt.plot(x,y,'--')
plt.plot(x,y1,'b')
plt.show()
