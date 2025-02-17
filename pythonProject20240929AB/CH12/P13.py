import  matplotlib.pyplot as plt
import  numpy as np
y1=[1,2,5,6,7,5,9,15]
y2=[4,5,6,7,8,11,20,5]
print(len(y1))
print(len(y2))
a=len(y1)+1
x=np.arange(1,a)
plt.figure(num=30,figsize=(8,5))
plt.plot(x,y1,'r-o')
plt.plot(x,y2,'g--')
#plt.xlim(3,7)
plt.xticks([1,3,5,7],('1','3','5','7'))
plt.grid()
plt.show()