"""
Baltimore City Analysis

Problem Statement:
Read the Baltimore.csv file
and perform the following task :

1. Remove the dollar signs in the AnnualSalary field and assign it as a float
2. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
3. How many employees are there for each JobRoles and Graph it
4. List All the Agency ID and Agency Name
5. Find all the missing Gross data in the dataset
"""

import pandas as pd

import numpy as np

df = pd.read_csv('Baltimore.csv')


#1. Remove the dollar signs in the AnnualSalary field and assign it as a float

df['AnnualSalary'] = df['AnnualSalary'].astype(str)

df['AnnualSalary'] = df['AnnualSalary'].apply(lambda x: x.replace('$',''))

df['AnnualSalary'] = df['AnnualSalary'].astype(float)


#2. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.


# group the data
grouped = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean])

print(aggregated)

#3. How many employees are there for each JobRoles and Graph it

df['JobTitle'].value_counts()[0:10].plot(kind = 'bar')


#4. List All the Agency ID and Agency Name
agency_name_id = df[['Agency','AgencyID']]
agency_name_id.drop_duplicates(inplace=True)
print(agency_name_id)

# 5. Find all the missing Gross data in the dataset
filter1 = df['GrossPay'].isnull()
len(df['GrossPay'][filter1])
#or below approach
df['GrossPay'].isnull().sum()




