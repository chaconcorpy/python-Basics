import pandas as pd
mydataset={'cars':['bmw','volvo','ford'],
           'passings':[3,7,2]
           }
myvar=pd.DataFrame(mydataset)
print(myvar)
#  to check the pandas version in ide
print(pd.__version__)
# panda series: is like a colomn in a table is a one dimensional array holding data of any type
myvar=pd.Series(mydataset)
print(myvar)
# label is used to access a specified value
print(myvar[1])
# create  your own labels
myvar=pd.Series(mydataset,index=['x','y','z'])
print(myvar)
# keys/values objects as series
calories={'day1':420,'day2':380,'day3':390}
myvar=pd.Series(calories)
print(myvar)
# in pandas the keys of the dictionary become the labels
# create a series using only data type from 'day1' and 'day2'
myvar=pd.Series(calories,index=['day1','day2'])
print(myvar)
# data sets in pandas are usually multidimensional table,called dataframes.
# series is like a column and  a dataframe is the whole table
# create a dataframe from two series
data={
    'calories':[420,380,392],
    'daration':[50,40,45]
}
myvar=pd.DataFrame(data)
print(myvar)
# dataframe is a two dimensional data structure like two dimensional array,or a table with two rows and columns
# create a simple dataFrame :
horses={
    'name':['black horse','white horse','red horse'],
    'seat:no':[1,2,3,]
}
myvar=pd.DataFrame(horses)
print(myvar)
# to locate the one or more specified row ,use loc() function
print(myvar.loc[0])
# to locate more than one row
print(myvar.loc[[0,1]])
# with the index argument ,you can name your own indexes
myvar=pd.DataFrame(data,index=['day1','day2','day3'])
print(myvar)
# use the named index in the loc attribute to return the specified row(s)
print(myvar.loc['day1'])
# load a comma separated file(CSV file) into a dataframe
df=pd.read_csv('data.csv')
print(df)
# CSV (comma separated files)
# CSV file is used as data interchange format due to their simplicity
# the other alternative of CSV is JSON(Javascript Object Notation) and XML(Extensible Markup Language)

myvar=pd.read_csv('data.csv')
print(myvar.to_string())
# check the number of maximum returned rows:
print(pd.options.display.max_rows)
# the above code line returned the 60 number of rows, which means that the print(myvar) statement will return only the headers and the first and last 5 rows
# you can increase the maximum number of rows to display the entire dataframe
pd.options.display.max_rows=9999
myvar=pd.read_csv('data.csv')
print(myvar)
# pandas read json
# load the JSON file into a dataFrame
myvar=pd.read_json('data.json')
print(myvar.to_string())
# json have the same format as python dictionaries
# analysing dataFrame
# viewing the data
# one of the most used method for getting a quick overview of the dataFrame,is the head() method
# the head method return the header and specified number of rows starting from the top
myvar=pd.read_csv('data.csv')
print(myvar.head(20))
# if the number of rows is not specified ,the head() method will return the top 5 rows
# there is also a tail() method for viewing the last rows of the dataframe.
# the tail method will return the headers and a specified number of rows,starting fromt the bottom
print(myvar.tail())
# print the information about the data
print(myvar.info())
# data cleaning: means fixing bad data in your data set:
# bad data could be :
'''
*empty cells
*data in wrong format
*wrong data
*duplicates
'''
# cleaning empty cells
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130,inplace = True)

print(df)


#Notice in the result that some rows have been removed (row 18, 22 and 28).

#These rows had cells with empty values.
# replace the empty value with mean ,median ,and mode
# calculate the mean and replace empty values with it
myvar=pd.read_csv('data.csv')
print(myvar.to_string)
# to remove the empty cell in csv file
myvar.dropna()
print(myvar.to_string)
x=myvar['Calories'].median()
myvar['Calories'].fillna(x,inplace=True)
# cleaning data of wrong format
# fixing wrong data
myvar.loc[7,'Daration']=45
print(myvar.to_string)
# plot a graph using pandas
import matplotlib.pyplot as plt
myvar.plot()
plt.show()
# scatter plot
myvar.plot(kind='hist',x='Duration',y='Calories')
plt.show()

