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
#we need to convert categorical(non numeric) data to numeric representation
#encode our categorical data in numeric
#onehotencoding

#info -> encoded (Morse code) -> transmission -> decode -> info

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )

import numpy as np
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

"""
features of data must be independant
so we must have to remove redudant features from the data 

"""
features = features[:,1:] #hadnling dumy variable trap 

#train test split
from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

#model

regressor.fit(features_train, labels_train)

pred = regressor.predict(features_test)

pd.DataFrame(zip(pred, labels_test))

pred_train = regressor.predict(features_train)

pd.DataFrame(zip(pred_train, labels_train))


regressor.score(features_train, labels_train)

regressor.score(features_test, labels_test)


#development, 1100, 2, 3 -> salary




x = ['UX',1100, 2, 3] #list
#it will thorough an error if we use value out of context ,'operations'

x = np.array(x)

x = x.reshape(1,4)

x = np.array(cTransformer.transform(x), dtype = np.float32)
#if we use fit_transform here it will override previous fit_transform


x = x[:,1:]
regressor.predict(x)





