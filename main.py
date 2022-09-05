import  pandas as pd

df = pd.read_csv('pokemon_data.csv')

# to read file slowly 
for df in pd.read_csv("pokemon_data.csv" ,chunksize= 100):
    print(df)

# print(df.head(3))
# print(df.tail(3))

#print headers
# print(df.columns)
# # read specific data by refrencing coulom name
# print(df["Name"][:-5])
#
# # refreance two or more coulums
# print(df[["Name" ,"Type 1"]])

# # print spcific rows
# print(df.iloc[5:10])

# # get specific spot
# print(df.iloc[2,3])

# # iterate throgh rows
# for index ,row in df.iterrows():
#     print(index , row['Name'])

#
# # find data based on value
# print(df.loc[df['Type 1']=="Fire"])

# #general desription of the df
# print(df.describe())

# # get data sorted
# print(df.sort_values(['Type 1',"HP"],ascending= False))


#makeing changes to the data

# # # add column with data based on values in other coulumns
df["Total"] = df["HP"] + df["Attack"]
# print(df)
#
# df = df. drop(columns= ['Total'])
# print(df)

# #save df to csv
# df.to_csv('modifed.csv')

# fillter data

# # find data by multible conditions
# print(df.loc[(df['Type 1']=="Grass") | (df['Type 2']=="Poison")])

# filer by not with ~
# filter by str containing with .str.contains
# print(df.loc[~df['Type 1'].str.contains(" Grass") ])


# filter with regex
# import re
# # print(df.loc[df['Type 1'].str.contains(" fire|grass" ,regex = True, flags = re.IGNORECASE)])
# #or
# print(df.loc[df['Name'].str.contains("^pi[a-z]*" ,regex = True, flags = re.IGNORECASE)])


# # change peice of data in whole document
# df.loc[df['Type 1']=="Fire" ,"Type 1"] = 'Flame'
# print(df)

# change based on other pecie of data
# df.loc[df['Type 1']=="Fire" ,"Legendary"] = True
# # all rows that are fire are lenendary
# print(df)

# #modify sevral rows based on contition
# df.loc[df['Total']> 50 ,["Legendary", "Generation"]] = ["Leg Val", "Gen Val"]
# print(df)


##############
#Statistics###
##############
# the following will find type1 values and sort the rest of the values by mean
print(df.groupby(['Type 1']).mean().sort_values("HP", ascending= False))
# you can also use sum and count(how many of each value) instead of mean

# you can also group by more than one coulum
print(df.groupby(['Type 1','Type 2']).count())
