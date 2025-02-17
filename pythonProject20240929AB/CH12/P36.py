import  matplotlib.pyplot as plt
import  numpy as np
city=['Delphi','Beijing','Washington','Tokyo','Moscow']
print(len(city))
pos=np.arange(len(city))
print(pos)
happing_index=[60,40,70,65,85]
plt.bar(pos,happing_index)
plt.xticks(pos,city)
plt.yticks([20,40,60,80,100],('very bad','bad','general','good','very good'))
plt.xlabel('capital')
plt.ylabel('index',rotation=0)
plt.title('barchart')
plt.show()
