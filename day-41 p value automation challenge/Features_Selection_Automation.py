"""
Code Challenge

In feature selection session, we wrote the feature removal code based on 
p value as manual removal activity after every summary cycle.

Automate the code where you do not need to manually check for 
pvalue and remove the corresponding column/feature.

"""



# Importing the libraries
import pandas as pd
import numpy as np


# Importing the dataset
dataset = pd.read_csv('Salary_Classification.csv')


dataset.shape

dataset.columns

dataset.dtypes

dataset.isnull().any(axis = 0)


#features and labels
#0,1,2,3 
features = dataset.iloc[:,0:4].values
labels = dataset.iloc[:,-1].values

#department columns
#we need to convert categorical data to numeric representation
#encode our categorical data in numeric
#onehotencoding

#info -> encoded (Morse code) -> transmission -> decode -> info

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )


features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]


# Building the optimal model using Backward Elimination
import statsmodels.api as sm
import numpy as np


#adds a constant column to input data set.
features = sm.add_constant(features)


# add code to automate the p value removing


features_optimal = features[:, [0,1,2,3,4,5]]

while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_optimal = np.delete(features_optimal, p_values.argmax(),1)
    else:
        break

    
print (features_optimal.shape)
#so ony exp is important for salary decision

