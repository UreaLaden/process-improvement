import pandas as pd

df=pd.read_csv('preDataset1.csv')
df.isnull().sum
print(df)
print()
print("Data Frame after replacing NaN with the Mean of the column")

df.B = df.B.fillna(df.B.mean())

print(df)