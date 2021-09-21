
# -*- coding: utf-8 -*-
""" A program to analyze the thanksgiving 2015 dataset """

# Importing the required modules for data preprocessing and visualizing
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Importing re module for using it in filtering out the income column
import re



# Encoding of the dataset is in Windows 1252 so it should be specified while loading it
thanksgiving_df = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

#replace the column names by number codes.

# Fetching the columns name for further reference
columns_name = thanksgiving_df.columns.tolist()

print (columns_name)

# Initializing a code number for each column name
columns_code = [x for x in range(0, 65)]

# Storing the column name with their codes for further reference
columns_names_code_mapping = dict(zip(columns_code, columns_name))

# Initializing the dataframe with the codes of the column
thanksgiving_df.columns = columns_code



# Fetching the data of the people who perform thanksgiving.

thanksgiving_df = thanksgiving_df[thanksgiving_df[1] == "Yes"]


#check for missing values
thanksgiving_df.isnull().any(axis = 0)

# Filling out the nan values with 'Missing' keyword
thanksgiving_df = thanksgiving_df.replace(np.nan, 'Missing')

# Analysing for the state/region, area  and income based what is consumed in thankgiving dinner
region_based = thanksgiving_df.groupby(64)
print (region_based.groups)
print (region_based.size())



income_based = thanksgiving_df.groupby(63)
print (income_based.groups)
print (income_based.size())


area_type_based = thanksgiving_df.groupby(60)
print (area_type_based.groups)
print (area_type_based.size())



# Analysis of the sauces prefered by each incomes group people
sauce_type_per_income_group = thanksgiving_df.groupby(8)[63].value_counts()

print (sauce_type_per_income_group)


#What is your gender? convert column to numeric values. 
#We’ll assign 0 to Male, and 1 to Female. 

# Filtering the gender and income columns using .apply method
def gender_filter(value):
    if value == "Male":
        value = 0
    elif value == "Female":
        value = 1

    return value

thanksgiving_df[62] = thanksgiving_df[62].apply(gender_filter)
print (thanksgiving_df[62].value_counts(dropna = False))




#income cleanup
thanksgiving_df[63] = thanksgiving_df[63].replace(['Prefer not to answer', 'Missing'],['0','0'])

regex = re.compile("\d+\W*\d+")

# A function to be passed in .apply() method for filtering out the salaries
def income_filter(value):
    value = regex.findall(value)
    value = [int(x.replace(",", "")) for x in value]
    return sum(value)/(len(value)+0.1)


# Using the apply method to filter the income column
thanksgiving_df[63] = thanksgiving_df[63].apply(income_filter)




# Fetching the average incomes for each type sauces

income_by_sauce_type = thanksgiving_df.groupby(8)[63]

print (income_by_sauce_type.groups)

avg_income_by_sauce_type = income_by_sauce_type.mean()

print (avg_income_by_sauce_type)



# Visualizing the average income of the various sauces
avg_income_by_sauce_type.plot.bar()
