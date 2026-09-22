import pandas as pd
print(pd.__version__)
# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#Think of it like a single column in a spreadsheet (1-Dimensional)
#This is a Constructor

data=[100,102,104]
series=pd.Series(data)
print(series)
#Output
# 0    100
# 1    102
# 2    104
# dtype: int64

# dtype specifies the data type of the specific elements integer means int 64 boolean shows bool string characters show object and float means float 64


new_series=pd.Series(data,index=['a','b','c'])
print(new_series)

#You can change the index of a value by the next attribute

print(new_series.loc['a'])

#To find the specific value of any data you can acess it by specifying its index values sort of like dictionary

print(new_series)
new_series.loc['c']=20
print(new_series)

#Output
# a    100
# b    102
# c    104
# dtype: int64
# a    100
# b    102
# c     20
# dtype: int64

#To change the value of the given index of a series by loc method
print(new_series)
print(new_series.iloc[1])
print(new_series.iloc[0])
print(new_series.iloc[2])

# Output
# a    100
# b    102
# c     20
# dtype: int64
# 102
# 100
# 20
#You can print the values of the series bu also using the original and primitve index values of the numbers

print(series[series>=100])