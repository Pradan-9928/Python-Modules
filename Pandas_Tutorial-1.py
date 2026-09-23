import pandas as pd
data=[0,101,203,190,700,604]
series=pd.Series(data)
print(series[series>500])

# the above example is one of the kind to filter out and display values of the speicific condition

calories={"pizza":200,"burger":300}
dict_series=pd.Series(calories)
dict_series.loc["burger"]+=100
print(dict_series.loc["burger"])