
import pandas as pd


df = pd.read_csv('Salaries.csv')

type(df)

df.shape

df.head()

df.head(3)

df.tail(2)

df.sample(3)

df['rank']

df['salary']

#df('rank')

df[['rank','salary']]

df['rank'].unique()

df['rank'].value_counts()


df['sex'].unique()

df['salary'].max()
df['salary'].min()
df['salary'].mean()

#-----------------------------

df.columns.tolist() #return as a list 

df['salary']
df.salary

df['rank']
df.rank

df['salary'] > 100000 #will return only true or false data 

filter1 = df['salary'] > 100000
df[filter1]


df[df['salary'] > 100000]



df[(df['salary'] > 100000) & (df['sex'] == 'Female')]


df.isnull().any(axis = 0) #it will check for the null values columns wise

df.isnull().any(axis = 1) #it will check for the null values row wise 

df[df.isnull().any(axis = 1)] #we can check which records are NaN. 
#---------------------------------------

"""
so we have to replace NaN with some number so one strategy is we can use mean of 
that particular coloumn 
"""
#---------------------------------------

df['phd'].mean()

#fillna() this function will replace all the nan data with given data.

df['phd'] =  df['phd'].fillna(df['phd'].mean())

df2 = df.fillna(100) #it will replace all the nan with 100 on entire data frame

df.dropna(inplace = True) #it will remove all the missing data from df 

df = pd.read_csv('Salaries.csv')

#iloc : interger loc, to access df with specific row and coloumn 
df.iloc[0:10,2:4]

df.iloc[10,:]

df.iloc[[10,15],:]

df.iloc[:,2]

