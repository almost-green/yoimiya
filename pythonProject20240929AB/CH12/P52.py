import matplotlib.pyplot as plt
import numpy as np
value1 = [82, 76, 24, 40, 67, 62, 75, 78, 71, 32, 98, 89, 78, 67, 72, 82, 87, 66, 56, 52]
value1_np=np.array(value1)
print('筆數:',len(value1_np))
print('平均:',np.mean(value1_np))
print('中位數:',np.median(value1_np))
print('為什麼平均與中位不是最多資料?')
print('hist顯示+紅色的平均線+黑色的中位數直線')
plt.axvline(np.mean(value1),0,1,c='r')
plt.axvline(np.median(value1),0,1,c='black')
plt.hist(value1)
plt.show()
