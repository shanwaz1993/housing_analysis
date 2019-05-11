# -*- coding: utf-8 -*-

import pandas as pd

data=pd.read_csv(r'/home/shan/Downloads/Melbourne_housing_FULL.csv',index_col=0)
#print(data.describe())
#print(data.info)

#print("Sample data")
#print(data.head())

#print(data.isnull().any())
print(data.dtypes)
df=data.select_dtypes(include='object')
print(df.columns)