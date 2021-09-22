
"""
Write a Python code that fulfills the following specification.
dataset: IQ_size.csv



It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

Task01:
What is the IQ of an individual with a given 
brain size of 90, height of 70 inches, and weight 150 pounds ? 

Task02:
Are a person's brain size and body size (Height and weight) predictive 
of his or her intelligence?

"""


# Importing the libraries

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('IQ_Size.csv')

features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)


"""
Task01:
What is the IQ of an individual with a given 
brain size of 90, height of 70 inches, and weight 150 pounds ? 

"""
regressor.predict([[90,70,150]])

#IQ based on above values: array([105.76890364])




# Building the optimal model using Backward Elimination

import statsmodels.api as sm

features = sm.add_constant(features)

features_sm = features[:,[0,1,2,3]]

est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

#remove weight column

features_sm = features[:, [0, 1, 2]]
est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

#drop constant

features_sm = features[:, [1, 2]]
est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

#drop the height


features_sm = features[:, [1]]
est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

print ("Brain Size is the only factor which is more useful in predicting intelligence.")




