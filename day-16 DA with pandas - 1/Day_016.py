"""
pandas use for data manupi lation analysis 
internaly it uses C 
EDA : exploratary data analysis 
       initial investigation about data 
pandas will load the data(read-csv) in data frame(tabular form in main memory)(row , coloumn)
pandas add index coloum in dataframe
to check the version of pandas : pd.__version__
list of funtions in pd : dir(pd)
to know about specific fucntion : help(pd.read_csv)
"""
import pandas as pd


df = pd.read_csv('Salaries.csv')
type(df)
df.shape #(row,coloumn)
df.head() #show intial 5 row 
df.tail(2) #show you last 2 row
df.sample(3) #show you 3 row (choose random)
df.coloumns #show you all the coloumns name , terminal 
df['rank']
df['salary']
#df('rank')

df[['rank','salary']]

df['rank'].unique() #show unique values 

df['rank'].value_counts() #output shown below 
# prof      46
# asstprof  19
# assocprof 13
# name: rank,dtype: int64

df['rank'].value_counts(normalize=True) #output will be in percentage 
# prof      0.589744
# asstprof  0.243590
# assocprof 0.166667
# name: rank,dtype: int64

df['sex'].unique()

df['salary'].max()
df['salary'].min()
df['salary'].mean()


