import pandas as pd
import numpy as np
company=["A","B","C"]
data1=pd.DataFrame(
{"company":[company[x] for x in np.random.randint(0,len(company),20)],
"salary":np.random.randint(5,50,20),
"age":np.random.randint(15,50,20)}
)
print(data1)
group = data1.groupby("company")
print(group)
print(list(group))
print(group.size())
print(group.first())
print(group.last())