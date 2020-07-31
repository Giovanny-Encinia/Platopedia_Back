import pandas as pd
import numpy as np

#First, I check the structure of the "xls" file, and I could determine which sheets I can to use for the analysis.
xls = pd.ExcelFile("FoodCompAfricaWest.xlsx")
food = pd.read_excel(xls, 2)

#I eliminate the "\n" in the columns' name
columns = food.columns.to_list()
columns = [element.replace('\n', ' ').upper() for element in columns]
food.columns = columns

#I will eliminate the rows with a number of N/A values greater than 44 also I will eliminate the first two rows
condition = food.isna().sum(axis=1) > 44
food.drop(food[condition].index, inplace=True)
food.drop(index=[0,1], inplace=True)

#In own dataframe in the last column exist diferent types of data so I handle the data and I eliminated the "[]", and I maked new data for a new column that will especify the method by wich the creators of the table found the phytatic acid.
columns = food.columns
columns = columns[5:]

for col in columns:
    lista = food[col].to_list() # Data of the last column of Food df
    method = [] # New column in own dataframe
    copy_lista = lista[:]
    i = 0

    for num in copy_lista:

        try:
            if num.find("[") != -1:
                method.append(1)
                num = num.replace("[", "")
                num = num.replace("]", "")
                lista[i] = num
                ward = 1
            else:
                method.append(0)

        except AttributeError:
            method.append(0)

        i += 1
    
    if ward == 1:
        food[col] = lista
        food[col + ' METHOD'] = method

#I change the data type of each column
for col in columns:
    food[col] = pd.to_numeric(food[col], errors="coerce")

#Now, I will find the food group's names
condition_sep = food.isna().sum(axis=1) > 43
group_index = food[condition_sep].index.to_list()

#I will create the diferents dataframe of the groups of food
#The name of the list of dataframe groups is group_food
group_food = [] # Save the data
copy = group_index[:] # Ward for handling data

try:
    
    for index in group_index:
        iterador = iter(copy)
        copy.pop(0) # eliminate the first element of copy in each iteration
        next_index = next(iterador)
        begin = index
        end = next_index - 2
        # I use 2 because previously I erased the row
        group_food.append(food.loc[begin: end])
        
except StopIteration:
    begin = group_index[-1]
    end = food.iloc[-1].name
    group_food.append(food.loc[begin: end])

#Se crea una lista en la cual se encuientran los distintos grupos de alimentos ( frutas, vegetales, raices, etc) abajo hay un ejemplo

# group_food[1].index.name  = food.loc[begin][0]
# group_food[1]