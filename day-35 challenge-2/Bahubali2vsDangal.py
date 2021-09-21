"""
    It contains Data of Day wise collections of the bollywood movies 
    Bahubali 2 and Dangal (in crores) for the first 9 days.    

    Now, you have to write a python code to develop a machine learning 
    model based on linear regressor to predict which movie would collect 
    more money on the 10th day.

file name "Box_Office.csv"

"""

import pandas as pd


dataset = pd.read_csv("Box_Office.csv")

#print dataset.describe()
feature = dataset.iloc[:, 0:1].values
label_bahubali = dataset.iloc[:, 1:2].values   # Bahubali 2
label_dangal = dataset.iloc[:, 2:3].values   # Dangal



from sklearn.linear_model import LinearRegression

regressor1 = LinearRegression() #model for bahubali
regressor1.fit(feature, label_bahubali) 

regressor2 = LinearRegression() #model for dangal
regressor2.fit(feature, label_dangal)

day = 10

#predict the collection for bahubali on 10th day

bahubali_collection = regressor1.predict([[day]])


dangal_collection = regressor2.predict([[day]])



if bahubali_collection > dangal_collection:
 print ("Therefore, Bahubali 2 will earn more on the {0}th day".format(day))
else:
 print ("Therefore, Dangal will earn more on the {0}th day".format(day))
 
 
 
 
#version 02

feature = dataset.iloc[:, 0:1].values
label_bahubali_dangal = dataset.iloc[:, 1:3].values   # Bahubali 2 and dangal




from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression() #model for bahubali
regressor1.fit(feature, label_bahubali_dangal) 


day = 10

#predict the collection for bahubali on 10th day

collections = regressor1.predict([[day]])

bahubali_collection, dangal_collection = collections[0]



if bahubali_collection > dangal_collection:
 print ("Therefore, Bahubali 2 will earn more on the {0}th day".format(day))
else:
 print ("Therefore, Dangal will earn more on the {0}th day".format(day))
 

 
 
 
 
 
 
 