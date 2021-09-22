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

#train test split
from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)


#feature scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train = sc.fit_transform(features_train)
#80%
#fit -> mean, std
#transform -> formula


features_test = sc.transform(features_test)
#20%
#fit_transform, fit - mean, std
#transform _ mean, std from tain data




from sklearn.linear_model import LinearRegression

#create object
regressor = LinearRegression()

#model


regressor.fit(features_train, labels_train)


pred = regressor.predict(features_test)



pd.DataFrame(zip(pred, labels_test))


pred_train = regressor.predict(features_train)



pd.DataFrame(zip(pred_train, labels_train))

#score
#train score
regressor.score(features_train, labels_train)
#predict(features_train)
#compare with labels_train

#test score


regressor.score(features_test, labels_test)


#development, 1100, 2, 3 -> salary




x = ['Development',1100, 2, 3]

x = np.array(x)

x = x.reshape(1,4)

x = np.array(cTransformer.transform(x), dtype = np.float32)


x = x[:,1:]
#transform

regressor.predict(x)





