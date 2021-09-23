"""
For this Code Challenge, The National Longitudinal 
Study of Adolescent to Adult Health (Add Health) 
data set, an ongoing (longitudinal) 
survey study that began in the mid-1990s is used. 
The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the 
University of North Carolina's
Carolina Population Center, 
#http://www.cpc.unc.edu/projects/addhealth/data.


Import addhealth.csv

 
The attributes are:

 
BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)


Explanatory Variables:


Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

 

Build a classification model evaluating if an adolescent 
would smoke regularly or not based on: 
gender, age, (race/ethnicity) Hispanic, White, 
Black, Native American and Asian, alcohol use, 
alcohol problems, marijuana use,
cocaine use, 
inhalant use, 
availability of cigarettes in the home, depression,
and self-esteem.

Build a classification model evaluation if an 
adolescent gets expelled or not from school based 
on their Gender and violent behavior.


Please make confusion matrix and also check accuracy 
score for each and every model.

"""
import pandas as pd
# Reading data from csv

df = pd.read_csv("addhealth.csv")

df.isnull().any(axis = 0)
# Removing NaN values with Most Frequent value of the column
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])



######## USING LOGISTIC REGRESSION ########

######## Solution for Part 1 ########
'''Build a classification model evaluating if an adolescent would smoke 
regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, 
Black, Native American and Asian, alcohol use, alcohol problems, marijuana use,
cocaine use, inhalant use, availability of cigarettes in the home, depression,
and self-esteem.'''

# Separating data into Independent and Dependent Variables
# Separating Dependent and Independent variables as per Problem Statement
features = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           
           'DEP1','ESTEEM1']].values
labels = df["TREG1"].values
    
# Splitting the dataset into train and test
from sklearn.model_selection import train_test_split as TTS

features_train,features_test,labels_train,labels_test = TTS(features, labels, test_size = 0.25,
                                    random_state = 0)

# Logistic Regression Model
from sklearn.linear_model import LogisticRegression
classification_treg1 = LogisticRegression(random_state=0)
classification_treg1.fit(features_train, labels_train)

pred = classification_treg1.predict(features_test)   # Prediction on test data   

# Confusion Matrix
from sklearn.metrics import confusion_matrix
classification_treg1_cm = confusion_matrix(labels_test, pred)

# check the accuracy on the Model
classification_treg1_score = classification_treg1.score(features_test, labels_test)
    


print ("model accuracy using confusion matrix (LogisticRegression): "+str(classification_treg1_cm))
print ("model accuracy using .score() function (LogisticRegression): "+str(round(classification_treg1_score*100,2)))


######## Solution for Part 2 ########
#an adolescent gets expelled or not from school


'''Build a classification model evaluation if an adolescent gets expelled or
 not from school based on their gender and violent behavior.'''


features_expel = df[["BIO_SEX","VIOL1"]].values
labels_expel = df["EXPEL1"].values


    
# Splitting the dataset into train and test
from sklearn.model_selection import train_test_split as TTS

f_train,f_test,l_train,l_test = TTS(features_expel, labels_expel, test_size = 0.25,
                                    random_state = 0)

# Logistic Regression Model
from sklearn.linear_model import LogisticRegression
classifier_expel = LogisticRegression(random_state=0)
classifier_expel.fit(f_train, l_train)

Pred1 = classifier_expel.predict(f_test)   # Prediction on test data   

# Confusion Matrix
from sklearn.metrics import confusion_matrix
CM1 = confusion_matrix(l_test, Pred1)

# check the accuracy on the Model
Score1 = classifier_expel.score(f_test, l_test)
    


print ("model accuracy using confusion matrix (LogisticRegression): "+str(CM1))
print ("model accuracy using .score() function (LogisticRegression): "+str(round(Score1*100,2)))




######## USING KNN ########


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split as TTS
from sklearn.metrics import confusion_matrix, accuracy_score

# Applying KNN Classifier
classifier_knn = KNeighborsClassifier(n_neighbors = 8)


######## Solution for Part 1 ########

# Separating Dependent and Independent variables as per Problem Statement
fe = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
la = df["TREG1"].values

# Splitting the Data into Test and Train
ft_train,ft_test,l_train,l_test = TTS(fe,la,test_size=.2,random_state=0)


classifier_knn.fit(ft_train,l_train)
pred_knn = classifier_knn.predict(ft_test)

# Building Confusion Matrix
CM = confusion_matrix(pred_knn,l_test)

# Getting Accuracy Score of the Model
Score = accuracy_score(l_test,pred_knn)
print ("model accuracy using confusion matrix (KNN): "+str(CM))
print ("model accuracy using .score() function (KNN): "+str(round(Score*100,2))+"%")



######## Solution for Part 2 ########

# Separating Dependent and Independent variables as per Problem Statement
fe1 = df[["BIO_SEX","VIOL1"]].values
la1 = df["EXPEL1"].values

# Splitting the Data into Test and Train
ftr,fte,ltr,lte = TTS(fe1,la1,test_size=.2,random_state=0)


classifier_knn.fit(ftr,ltr)
Pred1 = classifier_knn.predict(fte)

# Building Confusion Matrix
CM1 = confusion_matrix(Pred1,lte)

# Getting Accuracy Score of the Model
Score1 = accuracy_score(lte,Pred1)

print ("model accuracy using confusion matrix (KNN): "+str(CM1))
print ("model accuracy using .score() function (KNN): "+str(round(Score1*100,2))+"%")

