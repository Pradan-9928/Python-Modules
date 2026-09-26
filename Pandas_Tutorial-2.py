import pandas as pd
df=pd.read_csv("Pokemon.csv",index_col="Name")
#print(df.to_string())
print(df["Height"].to_string())