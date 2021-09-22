"""
Code Challenge


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, 
in which married women were asked about their participation 
in extramarital affairs.

Description of Variables:

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.


Now, perform Classification using logistic regression 
and check your model accuracy using confusion matrix 
and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, 
since they should be treated as categorical variables. 

Careful from dummy variable trap for both!!


Percentage of total women actually had an affair.

(note that Increases in marriage rating and religiousness correspond 
to a decrease in the likelihood of having an affair.)

 Predict the probability of an affair for a random woman 
 not present in the dataset. 
 She's a 25-year-old teacher who graduated college, 
 has been married for 3 years, 
 has 1 child, 
 rates herself as strongly religious, 
 rates her marriage as fair, 
 and her husband is a farmer.


"""

import numpy as np
import pandas as pd

# Reading data from csv
dataset = pd.read_csv("affairs.csv")

# Separating data into Independent and Dependent Variables
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

def Model(features, labels):
    # Applying OneHotEncoding
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer
    
    col_to_ohe = [6,7]  # Columns to be OneHotEncoded
    ct = ColumnTransformer([("encoder", OneHotEncoder(), [6,7])], remainder = 'passthrough')
    features = ct.fit_transform(features)
    
    # Getting indexes for the columns to be dropped, to avoid dummy variable trap
    total_col, indexes = 0, []
    for col in col_to_ohe:
        unique_val_count = len(dataset.iloc[:,col].value_counts())
        total_col += unique_val_count
        indexes.append(total_col - unique_val_count)
    
    # Dropping the dummy variable trap columns
    features = np.delete(features, indexes, axis=1)
    
    # Splitting the dataset into train and test
    from sklearn.model_selection import train_test_split as TTS
    
    features_train,features_test,labels_train,labels_test = TTS(features, labels, test_size = 0.25,
                                        random_state = 0)
    
    # Logistic Regression Model
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state=0)
    classifier.fit(features_train, labels_train)
    
    pred = classifier.predict(features_test)   # Prediction on test data
    
    # Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(labels_test, pred)
    
    # check the accuracy on the Model
    mod_score = classifier.score(features_test, labels_test)
    
    # Preprocessing the new individual's data
    """
     She's a 25-year-old teacher who graduated college, 
     has been married for 3 years, 
     has 1 child, 
     rates herself as strongly religious, 
     rates her marriage as fair, 
     and her husband is a farmer.
        
    """
    val = np.array([3, 25, 3, 1, 4, 16, 4, 2]).reshape(1,-1)
    val = ct.transform(val)
    val = np.delete(val, indexes, axis=1)
    
    val_pred = classifier.predict_proba(val)  # Predicting Individual's value
    

    
    return pred,cm, mod_score,val_pred


Pred, CM, Score, val_Pred = Model(features,labels)

print ("model accuracy using confusion matrix : "+str(CM))
print ("model accuracy using .score() function : "+str(round(Score*100,2)))
print ("percentage of total women actually had an affair : "+str(round(dataset["affair"].mean()*100,2))+"%")
print ("probability of an affair for a random woman is : "+str(val_Pred))

