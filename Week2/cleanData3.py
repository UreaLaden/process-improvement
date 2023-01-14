import pandas as pd

#Load CSV for processing
df=pd.read_csv('IrisSubset1.csv')  

#Find all cells with NA values
df.isnull().sum 

print(df)
print()
print("Data Frame after replacing NaN with the Mean of the column")

#Fill NaN values in Column B with the column average
df.sepal_width = df.sepal_width.fillna(df.sepal_width.mean()) 

print(df)