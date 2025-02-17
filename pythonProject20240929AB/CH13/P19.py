import numpy as np
import pandas as pd
array1 = np.array([[10, 30],[20,40]])
df = pd.DataFrame(array1)
df1 = pd.DataFrame(
    array1, columns = ["col1", "col2"])
df2 = pd.DataFrame(
    array1,
    columns = ["col1", "col2"],
    index=['row1','row2'])
np1=np.array(df);print(np1);print('-'*70)
np2=np.array(df1);print(np2);print('-'*70)
np3=np.array(df2);print(np3);print('-'*70)