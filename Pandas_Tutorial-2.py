import pandas as pd
df=pd.read_csv("Pokemon.csv",index_col="Name")
#Selecting the Columns of the table
#If you would want only a shortened form of the data frame you could use print(df) directly
#Whereas if you want a full extended form of the data frame you would have to use to_string() function
# print(df.to_string())
print(df["Height"].to_string())
#Selecting the Rows of the table
# print(df.loc["Pikachu":"Mewtwo",["Weight","Height"]].to_string())
# print(df.iloc[25])

# Filtering = Keeping the rows that match a condition  
tall_pokemon=df[df["Height"]>=2]
print(tall_pokemon)
heavy_pokemon=df[df["Weight"]>=100]
print(heavy_pokemon)
legendary=df[df["Legendary"]==1]
print(legendary)


#Finding the highest or lowest value in a given column of a dataframe
highest_height=df[df["Height"]==df["Height"].max()]
print(highest_height)
lowest_weight=df[df["Weight"]==df["Weight"].min()]
print(lowest_weight)

#Filtering with two conditions in mind
water_fly_type=df[(df["Type1"]=="Water") & (df["Type2"]=="Flying")]
print(water_fly_type)

# Whole dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())


# Single column I
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())


# In group by you cannot print the group or rows directly you should take help of aggregate function that's the only way you can print a group by 
group=df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].max())
