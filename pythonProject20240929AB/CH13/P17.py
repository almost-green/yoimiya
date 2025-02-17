import  pandas as pd
groups=['Python','Django','Sqlite','Numpy','Security','Pandas']
numbers=[59,9,19,14,6,77]
group_dict={'groups':groups,'numbers':numbers}
df=pd.DataFrame(group_dict)
print(df)