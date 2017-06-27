import numpy as np
import pandas as pd


"""GLOBAL REPLACEMENT OR COMMON VALUE """
data1 = pd.DataFrame([[5,2.8,9],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,23],[1,2,3]])
print(data1)
data1.fillna(inplace=True,value=0)
print(data1)



"""COLUMN WISE REPLACEMENT OF VALUE """
data2 = pd.DataFrame([[5,2.8,9],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,23],[1,2,3]])
print(data2)
#fill col 1 NaN values with 1, col2 NaN values with 2, col3 NaN values with 3
data2.fillna(inplace=True,value={0:1,1:2,2:3})
print(data2)


"""REPLACE NaN with COLUMN MEAN """
data3 = pd.DataFrame([[5,2.8,9],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,23],[1,2,3]])
print(data3)
#Replace NaN from each with oolumn wise mean Value
data3.fillna(inplace=True,value=data3.mean())
print(data3)



"""Interpolate values ie specify the number to be fillter by specifying the METHOD- example - fill the valid number which is next to NaN"""
data4 = pd.DataFrame([[5,2.8,9],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,23],[1,2,3]])
print(data4)
#Replace NaN from each with oolumn wise mean Value
data4.fillna(inplace=True,method='ffill')
print(data4)