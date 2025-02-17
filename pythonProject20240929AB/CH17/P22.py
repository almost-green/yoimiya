import  matplotlib.pyplot as plt
import  numpy as np
x=np.arange(-100,101,1)
y=-3*np.power(x,2)-12*x+4
print('因為平方前面的係數是負數，所以會有最大值')
print(np.max(y))
print(x[y.argmax()])
plt.plot(x,y)
plt.grid()
plt.show()