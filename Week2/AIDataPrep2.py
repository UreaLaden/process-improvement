# Leaundrae Mckinney
# 14 January 2023

import numpy as np
import pandas as pd
from sklearn import preprocessing

#Remove Null Values from the dataset
df = pd.read_csv("IrisSubset1.csv")
df.isnull().sum 
df.sepal_width = df.sepal_width.fillna(df.sepal_width.mean())

#Convert DataFrame to Numpy Array
input_data = df.to_numpy()
print(input_data)

#Convert data to binary values depending in relation to the threshold
data_binarized = preprocessing.Binarizer(threshold=1.5).transform(input_data)

print("\nBinarized data after preprocessing:\n",data_binarized)
print()
print("Mean=",input_data.mean(axis=0))
print("Std Deviation=",input_data.std(axis=0))
