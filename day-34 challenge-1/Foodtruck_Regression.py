"""
You will implement linear regression to predict the profits for a food chain 
company.

    Suppose you are the CEO of a restaurant franchise and are considering
    different cities for opening a new outlet.    
    
    The chain already has food-trucks in various cities and you have data for profits
    and populations from the cities.    
    
    You would like to use this data to help you select which city to expand to next.    
    
    Perform Simple Linear regression to predict the profit based on the
    population observed if you set up your outlet in Jaipur?
    
    (Current population in Jaipur is 3.073 million)  
    
    Hint:
    
    A negative value for profit indicates a loss.
"""


import pandas as pd


dataset = pd.read_csv("Foodtruck.csv")


features = dataset.iloc[:,0:1].values
labels = dataset.iloc[:,1:2].values

#Splitting
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

#   Linear Regression
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

#fit the model

regressor.fit(features_train, labels_train)

#now perform the prediction for Jaipur city

"""
3.073 - scalar
[3.073] - vector, 1D
[[3.073]] - vector, 2D
"""

regressor.predict([[3.073]])

#As profit is coming negative, so it would be a loss
#hence not recommended to open the outlet in Jaipur

regressor.predict([[33.4]])
