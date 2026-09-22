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