import matplotlib.pyplot as plt
import numpy as np
h=np.array([159,169,174,165,163,155,180,190])
w=np.array([55,45,70,60,65,45,72,50])
print("身高的平均:",np.mean(h))
print("身高的中位:",np.median(h))
print("體重的平均:",np.mean(w))
print("體重的中位:",np.median(w))
#'散佈圖
pos = np.arange(len(h))
plt.scatter(h,w)
plt.show()
