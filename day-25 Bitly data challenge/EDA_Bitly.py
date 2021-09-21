
""" 
A program to fetch various information related to url shotener bit.ly
associated with USA Gov and applying pandas operations on them 
"""


import pandas as pd

import numpy as np

# Creating the dataframe of the json file containing all the url shortener hits
# pandas.read_json is convert json string to pandas object
# lines parameter reads the file as json object per line

json_df = pd.read_json("bitly.json", lines=True)



#task 01: Replace the 'nan' values with 'Missing' and ' ' values with 'Unknown' keywords

json_df.isnull().any(axis = 0) #check for the missing values

json_df = json_df.replace([np.nan, "Missing"], [" ", "Unknown"])



#task 02: Print top 10 most frequent time-zones from the Dataset
# Getting the top 10 timezones frequency using pandas method
json_df_tz = json_df['tz'].value_counts().head(10)


#task 03: Count the number of occurrence for each time-zone
# Getting frequency of each timezones
tz_count = json_df['tz'].value_counts()

#task 04: Plot a bar Graph to show the frequency of top 10 time-zones
# To draw the top 10 timezones frequnecy bar graph for a series we can use Series.plot.type()
json_df_tz.plot.bar()




#task 05: From field 'a' which contains browser information 
#and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    
# Spiliting the Fetched series of browser info. according to tokens
"""
nint, default -1 (all)
Limit number of splits in output. 

expandbool, default False
Expand the split strings into separate columns.

If True, return DataFrame/MultiIndex expanding dimensionality.

If False, return Series/Index, containing lists of strings.

"""
#The add_prefix() function is used to prefix labels with string prefix.

tokens_df = json_df['a'].str.split(n = 1, expand = True).add_prefix("Token_")

# Fetching the frequency of the browser capability
tokens_frequency = tokens_df['Token_0'].value_counts()



# Plotting bar graph for top 5 browser capability
tokens_frequency.head().plot.bar()

# Filling the missing values in the token parts with mising string
tokens_df = tokens_df.replace(np.nan, 'Missing')



#task 06:

# Classifying as windows os and non-windows os

# Initializing the os column as Not windows
tokens_df["os"] = 'Not Windows'

# Applying the conditions to find the windows os user and initializing their os column as Windows
tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"



