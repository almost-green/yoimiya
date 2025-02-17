import  matplotlib.pyplot as plt
import  numpy as np
x=np.arange(-100,101,1)
y=3*np.power(x,2)-12*x+4
print('因為平方前面的係數是正數，所以會有最小值')
print(np.min(y))
print(x[y.argmin()])
plt.plot(x,y)
plt.grid()
plt.show()
