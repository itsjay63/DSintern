import pandas as pd

dataset = pd.read_csv("student_scores.csv")

dataset.shape
dataset.columns

dataset.isnull().any(axis = 0)


features = dataset['Hours'].values #values will convert all the data into a list 

labels = dataset['Scores'].values


import matplotlib.pyplot as plt
plt.scatter(features,labels)



