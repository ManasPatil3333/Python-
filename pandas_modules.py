import pandas as pd

tbl = pd.Series(['Virat','Rohit','Bumrah','Jadeja'],index=['1','2','3','4'])
print(tbl)

s = pd.Series(['1','3','5','7','9'])
print(s.values)
print(s.index)

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],'age': [25, 30, 35, 40],'gender': ['F', 'M', 'M', 'M']}
df = pd.DataFrame(data)
print(df)
print(df.head(2))
print(df.tail(2))
print(df['name'])
print(df.loc[2])
