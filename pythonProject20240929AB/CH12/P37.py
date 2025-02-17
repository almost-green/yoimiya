import  matplotlib.pyplot as plt
import  numpy as np
city=['Delphi','Beijing','Washington','Tokyo','Moscow']
pos=np.arange(len(city))
gender=['Male','Female']
happing_index_male=[60,40,70,65,85]
happing_index_female=[30,60,70,55,75]
# plt.bar(pos,happing_index_female,color='pink')
plt.bar(pos,happing_index_male,color='blue')
plt.bar(pos,happing_index_female,color='pink')
plt.xticks(pos,city)
plt.xlabel('capital')
plt.ylabel('index',rotation=0)
plt.legend(gender,loc=2)
plt.title('barchart')
plt.show()