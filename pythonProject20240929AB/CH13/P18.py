import  pandas as pd
import  numpy as np
array1=np.array([[10,30],[20,40]])
print(array1)
df=pd.DataFrame(array1)
print(df)
print('dataframe的row與column的index')
df2=pd.DataFrame(
array1,columns=['col1','col2'],index=['row1','row2'])
print(df2)