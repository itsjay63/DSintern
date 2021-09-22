"""
In 1981, 78 bluegills were randomly sampled from Lake Mary in Minnesota. 
The researchers (Cook and Weisberg, 1999) measured and recorded the 
following data:
(Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish.

How is the length of a bluegill fish related to its age?

How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.



"""

# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, 0:1].values
labels = dataset.iloc[:, 1].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(len(features_grid), 1)
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, lin_reg.predict(features_grid), color = 'blue')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()



# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
higher_degree_gen = PolynomialFeatures(degree = 2)
features_poly = higher_degree_gen.fit_transform(features)
regressor_poly = LinearRegression()
regressor_poly.fit(features_poly, labels)


# Visualising the Polynomial Regression results (for higher resolution and smoother curve)

features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(len(features_grid), 1)
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, regressor_poly.predict(higher_degree_gen.fit_transform(features_grid)), color = 'blue')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()



print ("Predicting result with Linear Regression :"+str(lin_reg.predict([[5]])))


print ("Predicting result with Polynomial Regression :"+str(regressor_poly.predict(higher_degree_gen.fit_transform([[5]]))))






