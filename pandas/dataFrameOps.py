import pandas as pd
import datetime
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style


""" Data Reader - read from external source - Web

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

""" CREATE DF from dictionary

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


""" convert category variable to continous variable

stat_dict = {'name':['a','b','c','d','e','f'],
             'marks': ['good','poor','absent','poor','good','absent']}

stat_df = pd.DataFrame(stat_dict)
#print(stat_df)

mark_col = stat_df['marks']
print(mark_col)
"""

""" Method1: Finding unique values from column
mark_unique = set(mark_col)
#print(mark_unique)

#mark_uniquw also can be converted to array

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
"""


"""Method2: Finding unique values in column
makr_unique1 = stat_df['marks'].unique()

print(makr_unique1)
"""

"""Calculating moving average of time series data 

data1 = {'data':[1,2,3,4,5,6,7,8,9]}

df = pd.DataFrame(data1)

#use rolling function to mention number of element and then mention which method you would like to call on that
rolling_df = df.rolling(2).mean()

print(rolling_df)

plt.plot(df['data'])
plt.plot(rolling_df['data'])
plt.show()

"""

""" data selection in pandas
#https://www.youtube.com/watch?v=eM7p3MVLOZ8&list=PLA83b1JHN4ly2mOHrBZUUyRyhr8fO0p6l&index=9
df = pd.read_csv("train.csv")
print(df.head(5))


#select single column
print(df['Pclass'].head())

#select multiple columns
print(df[['Pclass','Fare']].head())

#select individual record by row index - iloc --> index location
print(df.iloc[3:5])

#select few cells..same iloc function with first element --> row number, comma seperated by column index
#example - rows - 0 to 4 cell number - 3
print(df.iloc[0:5,3])
"""

""" Conditional selection of data """
#https://www.youtube.com/watch?v=eM7p3MVLOZ8&list=PLA83b1JHN4ly2mOHrBZUUyRyhr8fO0p6l&index=10
df = pd.read_csv("train.csv")
print(df.head(5))

#print records with Fair > 10
print(df[df['Fare'] > 10])

#print records with Fair > 10 with only oclumn -- 'Fare'
print(df[df['Fare'] > 10]['Fare'])

#gender wise filter
print(df[df['Sex'] == 'male']['Sex'])

#negation in filter
print(df[df['Sex'] != 'male']['Sex'])