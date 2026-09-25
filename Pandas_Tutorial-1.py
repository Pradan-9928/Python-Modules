# import pandas as pd
# data={"Name":["Harry Potter","Hermione Granger","Ronald Weasley"],
#       "Blood":["Half Blood","Half Blood","Pure Blood"]}
# index=["Person1","Person2","Person3"]
# series=pd.DataFrame(data,index)

# print(series)

# print(series.loc["Person1"])

# #adding a new column in an existing dataframe

# series["Job"]=["Auror","Minister Of Magic","Auror"]

# #adding a new row in an existing dataframe
# new_row=pd.DataFrame([{"Name":"Sandy","Age":"28"}],index=["Person4"])
# series=pd.concat([series,new_row])

# print(series)

import pandas as pd
dict={"Name":["Tanjiro Kamado","Nezuko Kamado","Inosuke","Zenitsu"],
      "Age":[13,12,15,16]}
index=["Person 1","Person 2","Person 3","Person 4"]


df=pd.DataFrame(dict,index)
print(df)

df["TYPE"]=["Human","Demon-Part-Human","Human","Human"]
df["Gender"]="Nil"
new_row=pd.DataFrame([{"Name":"Yoriichi Tsugikuni","Age":"Dead","TYPE":"Human"}],index=["Person 5"])
df=pd.concat([df,new_row])
print(df)
