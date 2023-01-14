import pandas as pd
from sklearn import preprocessing

# df = pd.read_csv("preNormDataset1.csv")
df = pd.read_csv("IrisSubset1.csv")

print(df)
print()
print("Data Frame after Normalization")

x=df.values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)

df=pd.DataFrame(x_scaled,columns=df.columns)
print(df)