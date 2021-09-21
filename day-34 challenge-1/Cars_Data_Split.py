"""
Import the local file cars.csv and split the data set equally into test set 
and training set. 


"""


import pandas as pd


#version 01
# Importing the dataset
dataset = pd.read_csv('cars.csv')


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

dataset_train, dataset_test = train_test_split(dataset, test_size = 0.5, random_state = 0)

dataset_train.to_csv('dataset_train.csv', index = False)
dataset_test.to_csv("dataset_test.csv", index = False)





#version 02:
    
# Importing the dataset
dataset = pd.read_csv('cars.csv')



features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values #price is the labels


#print (dataset.columns.tolist())

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split



features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.5, random_state = 0)
