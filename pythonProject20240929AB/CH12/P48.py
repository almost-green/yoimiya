import matplotlib.pyplot as plt
import numpy as np
values=[60,80,90,55,10,30]
colors=['b','g','r','c','m','y']
labels=['US','UK','India','Germany','Australia','South Korea']
explode=(0.2,0,0,0,0,0)
plt.pie(values)
plt.show()
print('上面看不出來誰是誰')
plt.pie(values,labels=labels)
plt.show()
print('美國部份希望突出')
plt.pie(values,labels=labels,explode=explode)
plt.show()
