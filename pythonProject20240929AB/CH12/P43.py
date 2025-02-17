import matplotlib.pyplot as plt
import numpy as np
h=np.array([159,169,174,165,163,155,180,190])
w=np.array([55,45,70,60,65,45,72,50])
print(h)
print(w)
plt.scatter(h,w)
plt.xlabel('h')
plt.ylabel('w')
#plt.text(160,60,'test1',fontsize=20)
for temp1 in zip(h,w):
  print(temp1)
  plt.text(temp1[0], temp1[1],
           '(' + str(temp1[0]) + ',' + str(temp1[1]) + ')',
           fontsize=10)
plt.grid()
plt.show()
