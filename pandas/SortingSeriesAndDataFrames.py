import pandas as pd
import numpy as np


"""SORTING ON SERIES """
series = pd.Series(range(5),index=['a','e','b','d','c'])
print(series)
#sort series based on index
series.sort_index(inplace=True)
print(series)
#sort series on values
series.sort_values(inplace=True)
print(series)


#Sorting on series containing NaN values
#NOTE: NaN values are placed at the end for both the types of sortings - asc, desc
series_with_nan = pd.Series([1,np.NaN,5,2,np.NaN], index=['a','b','c','d','e'])
print(series_with_nan)
print("")
series_with_nan.sort_values(inplace=True)
print(series_with_nan)
print("")
""" OUTPUT OF ABOVE CODE IS 
a    1.0
d    2.0
c    5.0
b    NaN
e    NaN
dtype: float64
"""

#descending sorting
series_with_nan.sort_values(inplace=True,ascending=False)
print(series_with_nan)
print("")
"""
 OUTPUT OF ABOVE CODE LOOKS LIKE 
 
c    5.0
d    2.0
a    1.0
b    NaN
e    NaN
dtype: float64
"""



""" SORTING ON DATAFRAME """
df = pd.DataFrame(np.arange(8).reshape(2,4), index = [8,3], columns=['d','a','b','c'])
print(df)
print("")
#row based sorting
df.sort_index(inplace=True)
print(df)
print("")
#column based sorting
df.sort_index(inplace=True, axis=1)
print(df)
print("")
#sorting based on values
df.sort_values('a',ascending=True,inplace=True)
print(df)
