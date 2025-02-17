import matplotlib.pyplot as plt
import numpy as np
values=[60,80,90,55,10,30]
colors=['b','g','r','c','m','y']
labels=['US','UK','India','Germany','Australia','South Korea']
print('label希望呈現國家與數值')
labels2=[]
for temp1 in zip(labels,values):
  data1=str(temp1[0])+':'+str(temp1[1])
  labels2.append(data1)
#print(labels2)
plt.pie(values,labels=labels2)
plt.show()
