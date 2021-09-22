import pandas as pd

import matplotlib.pyplot as plt

dataset = pd.read_csv("Claims_Paid.csv")

dataset.dtypes

dataset.isnull().any(axis = 0)

features = dataset.iloc[:,0:1].values
#0 : 1d
#[0]:2d

labels = dataset.iloc[:,1:2].values

plt.scatter(features, labels)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(features, labels)

regressor.predict([[1981]])
#array([[106.03933333]])


plt.scatter(features, labels)
plt.plot(features, regressor.predict(features), color = 'red')

#here we have one feature and we converted it to higher dim. 
from sklearn.preprocessing import PolynomialFeatures

features_higher_degree = PolynomialFeatures(degree = 5)

features_ndata = features_higher_degree.fit_transform(features)

regressor_ndata = LinearRegression()


regressor_ndata.fit(features_ndata, labels)


plt.scatter(features, labels)
plt.plot(features, regressor_ndata.predict(features_higher_degree.transform(features)), color = 'red')


regressor_ndata.predict(features_higher_degree.transform([[1981]]))
#array([[148.44609171]])
