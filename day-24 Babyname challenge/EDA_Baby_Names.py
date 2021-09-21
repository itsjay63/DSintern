
#version 02
    
#task 01

#use glob to find out all the files in baby_names folder with .txt extention
import re
from glob import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#the glob module is used to retrieve the files
#or pathnames matching a pattern

filenames = glob('baby_names/*.txt')
    
ssa_df_list = []

for file in filenames:
    temp_df = pd.read_csv(file, names = ['names','sex','count'])
    #extract the year from file
    year = int(re.findall('\d\d\d\d', file)[0])
    
    if year > 2010: #we need to collect data from 1880 to 2010 only
        break

    #add a new colum to temp_df with name year and write int(year)
    #adding a new column with default value as year
    #simple is    
    temp_df['year'] = year
    #now append temp_df to ssa_final_df
    ssa_df_list.append(temp_df)
    
#now ssa_df_list contains 138 dataframes
    
#lets make a final df concatenating all of temp dfs in list

finaldf = pd.concat(ssa_df_list, axis = 0, ignore_index = True)
#finaldf.to_csv("babynames.csv")

#task 02: Display the top 5 male and female baby names of 2010.

df_2010 = finaldf[finaldf['year'] ==  2010]

female_names = df_2010[df_2010['sex'] == 'F']

female_names_sort_by_count = female_names.sort_values('count', ascending = False, ignore_index = True)

#top five female names of 2010
print (female_names_sort_by_count['names'][0:5]) 

#male names
male_names = df_2010[df_2010['sex'] == 'M']

male_names_sort_by_count = male_names.sort_values('count', ascending = False, ignore_index = True)

#top five female names of 2010
print (male_names_sort_by_count['names'][0:5]) 


#task 03:     Calculate sum of the births column by sex as the total number of births  
#in that year(use pandas groupby method).

grouped_multiple = finaldf.groupby(['year', 'sex']).agg({'count': ['sum']})

print(grouped_multiple)



#task 04: Plot the results of the above activity to show total births  by sex and year.

grouped_multiple.plot(kind='bar')

grouped_multiple[0:10].plot(kind='bar')










"""
You can also use below code for better visualization
#Getting the year list

x_val = []
for i in grouped_multiple.index:
    if i[0] not in x_val:
        x_val.append(i[0])
#Getting the count
yval = list(grouped_multiple['count']['sum'])


#Female count are on even place
y_val_f = [yval[i]  for i in range(0,len(yval)) if i%2==0]
#Male count are on odd place

y_val_m = [yval[i]  for i in range(0,len(yval)) if i%2!=0]


  
X_axis = np.arange(len(x_val[0:10]))
  
plt.bar(X_axis - 0.2, y_val_f[0:10], 0.4, label = 'Female')
plt.bar(X_axis + 0.2, y_val_m[0:10], 0.4, label = 'Male')
  
plt.xticks(X_axis, x_val[0:10])
plt.xlabel("Year, Sex")
plt.ylabel("Count")
plt.legend()
plt.show()


"""



