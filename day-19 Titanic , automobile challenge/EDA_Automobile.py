import pandas as pd
import matplotlib.pyplot as plt


# Reading CSV file
df = pd.read_csv('Automobile.csv')


'''1. Handle the missing values for Price column'''
#how the check the data type of a column
df['price'].dtype
#incase this column is not in float/int, 
#convert the datatype to float/int 
#before handling the missing values

# Converting the datatype of price column from object to flaot
df["price"] = df["price"].astype(float)

#check if this colums has really a missing data
#if it gives True -> this column has missing data else no missing data

df['price'].isnull().any(axis = 0)

# Filling the missing values with average of price column
df["price"] = df["price"].fillna(df["price"].mean())


'''2. Get the values from Price column into a numpy.ndarray'''
# Converting the price column into a numpy.ndarray
price_numpy_array = df["price"].values


'''3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price'''
print (df["price"].min())
print ( df["price"].max())
print (  round( df["price"].mean(), 2 ))
print ( round( df["price"].std(), 2 ) ) 


'''4. Make a pie chart for all car makers'''
# Make a pie chart for all car makers

series = df["make"].value_counts()

topCarMakers = series.index[0:11]
vehicleCount = series.values[0:11]

plt.pie(vehicleCount, labels=topCarMakers, autopct='%.2f%%')

plt.show()

