import pandas as pd


#simple series
series = pd.Series([1,6,2,9,5])
print(series)

print("")
#print values of series
print(series.values)

print("")
#specify the index to series
series1 = pd.Series([6,1,9,4,5], index=['a','d','b','c','e'])
print(series1)

#access values based on index
print(series1['b'])

#print indexes of elements for which condition is true
print(series1 > 4)

#acces elements based on condition
print(series1[series1 > 4])

#arithmatic on series
multiple = series1 * 2
print(multiple)


#assign the dictionary to Series
dict = {'pune':12, 'satara':11, 'kolhapur':35, 'karad':52,'mumbai':4}
print(dict)
dict_series = pd.Series(dict)
print(dict_series)
#access elements based on index
print(dict_series['satara'])