
import pandas as pd

dataset = pd.read_csv("caesarian.csv")

dataset.shape
dataset.columns.tolist()

dataset.dtypes

dataset.isnull().any(axis = 0)

#features, labels

features = dataset.iloc[:,0:5].values
labels = dataset.iloc[:,5].values

#train test split
from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

#build the model - classifier
#kNN - KneigbhorsClassifier

from sklearn.neighbors import KNeighborsClassifier


classifier = KNeighborsClassifier(n_neighbors = 5, p = 1)
#p = 1, manhanttan
#p = 2, euclidian


classifier.fit(features_train, labels_train)

classifier.predict(features_test)











