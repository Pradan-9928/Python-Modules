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
