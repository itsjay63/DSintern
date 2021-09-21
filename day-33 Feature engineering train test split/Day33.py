import pandas as pd

dataset = pd.read_csv("student_scores.csv")


#split the data in two sets
#train set - training the model
60 - 80%
#test set - we evaluate how good or bad your model is
40 - 20% 
#train test split



features = dataset['Hours'].values

labels = dataset['Scores'].values

##perform it (train test split)


from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)


from sklearn.linear_model import LinearRegression

#create object
regressor = LinearRegression()

#model
features_train = features_train.reshape(20,1)

regressor.fit(features_train, labels_train)

features_test = features_test.reshape(5,1)

pred = regressor.predict(features_test)



pd.DataFrame(zip(pred, labels_test))




 

"""

#list
#ndarray
#df

import numpy as np

list1 = [1,2,3,4,5,6,7,8,9,10]
array = np.arange(10)
#train_test_split will split data in 70-30 , and it will pick data randomly 
train, test = train_test_split(list1, train_size = 0.8, random_state = 41)
#here we can use test_size=0.2 instaed of train_size = 0.8 
#if we use more than one list,array here , split function will apply on all the 
#list, array given 
#if we give random_state.. it will provide same data again and again 



"""







