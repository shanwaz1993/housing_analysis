# -*- coding: utf-8 -*-

import pandas as pd

data=pd.read_csv(r'/home/shan/Downloads/Melbourne_housing_FULL.csv',index_col=0)

#take a look into data
print(data.describe())
#print(data.info)
#print(data.head())
#print(data.columns)
#print(data.index)
#print(data.dtypes)

#-----------categorization of data 
#print(data.isnull().any())
#df=data.select_dtypes(include='object')
#print(df.head())
#print(df.isnull().any())

#----------Measure of tandency 
#print(data['Regionname'].mode())
#print(df['CouncilArea'].mode())
#print(data['Price'].mean())
#print(data['Price'].median())


#--------measure of spreads
print(data['Price'].std())
print(data['Price'].var())
print(data['Price'].mad())


#print(data.mode())
#print(data[data.Rooms==1].loc[:,'Rooms':'Price'].count())
#print(data.loc[data.Rooms==1].Price)
#print(data[data.Rooms==2].loc[:,'Rooms':'Price'].count())
#print(data[data.Rooms==3].loc[:,'Rooms':'Price'].count())

#filter
#print(data[(data.Rooms==1) & (data.Price>2000000)].loc[:,'Rooms':'Price'])
#print(data[(data.Rooms==1) & (data.Price>2000000)].loc[:,'Rooms':'Price'].sort_values(['Price'],ascending=[0]))
#print(data[(data.Rooms==1) & (data.Price>2000000)].loc[:,'Rooms':'Price'].sort_values(['Rooms','Type','Price'],ascending=[0,1,1]))

#print(data[(data.Rooms==1) | (data.Rooms>2) & (data.Type=='u')].loc[:,'Rooms':'Price'])

#print(data[(data.Rooms!=3)&(data.Price>2000000)&(data.Type!='h')].loc[:,'Rooms':'Price'])



