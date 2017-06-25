import pandas as pd
import datetime
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style


""" Data Reader - read from external source - Web"""
"""
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2015,12,31)

df = data.DataReader("GOOG","google",start,end)

print(df.head(8))

print(df.tail(10))
print(df.size)
print(df.shape)
print(style.available)
style.use('seaborn-poster')

df.plot()
plt.show()
"""

""" CREATE DF from dictionary"""
"""
records_dict = {'name':['ashwini','aarti','shweta','shilpa' ],
                'surname':['barkade','verma','kalalabandi','math'],
                'roll_no':[50,60,70,80]}
records_df = pd.DataFrame(records_dict)

#print(records_df)

records_df.set_index('name',inplace=True)

print(records_df)

records_df.plot()
plt.show()

print(records_df.head(2))
print(records_df.tail(2))

"""

""" PANDAS I/O

boston_df = pd.read_csv("boston.csv")
print(boston_df.head())

boston_df.to_json("boston.json")
boston_df.to_html("boston.html")
"""

""" Add delete columns  

lst = [1,2,3,4,5,6]
lst_dataframe = pd.DataFrame(lst)
lst_dataframe.columns = ['numbers']
lst_dataframe['newCol'] = 3
lst_dataframe['newCol1'] = lst_dataframe['newCol'] + 5
lst_dataframe.index = [5,4,3,2,1,0]
#del lst_dataframe['newCol']
print(lst_dataframe)
print(lst_dataframe.columns)

"""

""" df properties

train_df = pd.read_csv("train.csv")
print(train_df.dtypes)
print(train_df.shape)
print(train_df.head())
print(train_df.describe())
print(train_df.info())

"""

""" convert category variable to continous variable"""

stat_dict = {'name':['a','b','c','d','e','f'],
             'marks': ['good','poor','absent','poor','good','absent']}

stat_df = pd.DataFrame(stat_dict)
#print(stat_df)

mark_col = stat_df['marks']
print(mark_col)

mark_unique = set(mark_col)
#print(mark_unique)

mapping_dict = {}
num = 0;
for item in mark_unique:
    mapping_dict[item] = num
    num= num+1

print(mapping_dict)

def convert(x):
    return mapping_dict[x]

stat_df['marks_cont'] = stat_df['marks'].apply(convert)

print(stat_df)