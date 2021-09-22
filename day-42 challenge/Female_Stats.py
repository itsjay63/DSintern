"""
Write a Python code that fulfills the following specification.
dataset: Female_Stats.csv


The Data Are From 214 Females In Statistics Classes At 
The University Of California At Davis.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. 

All Heights Are In Inches.

task01:
Build A Predictive Model And Conclude If Both Predictors 
(Independent Variables) Are Significant For A Students’ Height Or Not?
(Use pvalue concepts).

task02:
When Father’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Mother’s Height.

task03:
When Mother’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Father’s Height.

"""



# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Female_Stats.csv')

# Check data Types for each columns
print(dataset.dtypes)

# Seperate Features and Labels
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, [0]].values

# Check Column wise is any data is missing or NaN
dataset.isnull().any(axis=0)


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

Pred = regressor.predict(features_test)

print (pd.DataFrame(zip(np.round(Pred,2), labels_test)))



import statsmodels.api as sm

features_sm = sm.add_constant(features)
est = sm.OLS(labels, features_sm)
est2 = est.fit()

print (est2.summary())

"""
as both columns ( mom and dad are having p values less than 5%, both 
                 heights are significant for student's height)
"""

"""

When Father’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Mother’s Height.

"""

print (regressor.coef_[0][0])


"""

When Mother’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Father’s Height.



"""
print (regressor.coef_[0][1])


























# Version 2 of solution 




import pandas as pd
import numpy as np

dataset=pd.read_csv("stats_females.csv")

features=dataset.iloc[:,1:]
labels=dataset.iloc[:,0]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(features_train,labels_train)

import statsmodels.formula.api as sm
features=np.append(arr=np.ones((214,1)).astype(int),values=features,axis=1)

features_opt=features[:,[0,1,2]]
regressor_OLS=sm.OLS(labels,features_opt).fit()
regressor_OLS.summary()

"""
When Father’s Height Is Held Constant, The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Mother’s Height.
"""
print("When Father's Height is Held Constant then the average height increase by",regressor_OLS.params[1])

print("When Mother's Height is Held Constant then the average height increase by",regressor_OLS.params[2])