import pandas as pd

dataset = pd.read_csv("Salary_Classification.csv")

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

import numpy as np
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

"""




#train test split
from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

from sklearn.linear_model import LinearRegression

#create object
regressor = LinearRegression()

#model


regressor.fit(features_train, labels_train)


pred = regressor.predict(features_test)



pd.DataFrame(zip(pred, labels_test))


pred_train = regressor.predict(features_train)



pd.DataFrame(zip(pred_train, labels_train))

"""

#backward elimination
import statsmodels.api as sm 
#we can use statesmodels instade of sklearn to perform linear regression 
#OLS - optimal least square 


features = sm.add_constant(features)


#features, labels

features_optimal = features[:,[0,1,2,3,4,5]]

regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()

# p value

regressor_ols.summary()

regressor_ols.pvalues

#5% : p values should be less than 5% 
#if it is more than that it shows that it is not so important 
#7%
#also we can drop colums one at a time 

features_optimal = features[:,[0,1,3,4,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()

# p value

regressor_ols.summary()


features_optimal = features[:,[0,1,3,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()

# p value

regressor_ols.summary()


features_optimal = features[:,[0,3,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()

# p value

regressor_ols.summary()



features_optimal = features[:,[0,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()

# p value

regressor_ols.summary()





















