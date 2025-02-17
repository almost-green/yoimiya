import  numpy as np
import  matplotlib.pyplot as plt
values = [82, 76, 24, 40, 67, 62, 75, 78, 71, 32, 98, 89, 78, 67, 72, 82, 87, 66, 56, 52]
print(len(values))
x1=np.arange(len(values))
plt.bar(x1,values)
plt.show()
plt.hist(values,bins=5)
plt.show()

