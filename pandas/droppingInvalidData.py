import pandas as pd
import numpy as np

"""LOW LEVEL DROPPING OF INCOMPLETE DATA"""

""" dropnam for pandas series
#create pandas Series
Data = pd.Series([1,np.NaN,4,5,np.NaN,6])
print(Data)
#clear missing ie NAN data
Data.dropna(inplace=True)
print(Data)
"""

"""dropna for DataFrame
#dropna on DataFrame
data1 = pd.DataFrame([[5,2.8,9],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,23],[1,2,3]])
print(data1)
#NOTE: Whole row will get deleted if even one of the columns hav NaN
data1.dropna(inplace=True)
print("data1 after dropping the NaN:")
print(data1)
"""


"""Conditional drop. Drop only if all entries in row are NaN
data2 = pd.DataFrame([[5,2.8,9],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,23],[1,2,3]])
data2.dropna(inplace=True,how='all')
print(data2)
"""


"""COLUMN LEVEL DROPPING OF INCOMPLETE DATA

data3 = pd.DataFrame([[5,2.8,9],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,23],[1,2,3]])
print(data3)
#axis=1 signifies the column wise drop. So it will delete all the coulmns which has atleast one value as NaN
data3.dropna(axis=1,inplace=True)
print(data3)


data4 = pd.DataFrame([[5,2.8,np.NaN],[1.5,np.NaN,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,np.NaN],[1,np.NaN,np.NaN]])
print(data4)
#axis=1 signifies the column wise drop. So it will delete all the coulmns which has atleast one value as
#delete the column only if all the values are NaN
data4.dropna(axis=1,inplace=True,how='all')
print(data4)
"""


"""FILTER BASED ON THRESHOLD ie keeping values based on filter"""
data5 = pd.DataFrame([[5,2.8,np.NaN],[1.5,2,np.NaN],[np.NaN,np.NaN,np.NaN],[np.NaN,6.2,np.NaN],[1,np.NaN,np.NaN]])
print(data5)
#threshold--> retain the rows(axis=0 OR if not mentioned the axis) having atleast threshold number of valid entries
data5.dropna(inplace=True, thresh=1) #i.e retain the row if atleast one vaild number is present in row
print(data5)
data5.dropna(inplace=True, thresh=2) #i.e retain the row if atleast two vaild numbers are present in row
