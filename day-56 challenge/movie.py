"""
Import movie.csv file

There are two categories: 
Pos (reviews that express a positive or favorable sentiment)
and Neg (reviews that express a negative or unfavorable sentiment).

For this code challenge, we will assume that all reviews are 
either positive or negative;
there are no neutral reviews.

Perform sentiment analysis on the text reviews 
to determine whether its positive
or negative and build confusion matrix to determine the accuracy.

"""

# Natural Language Processing

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('movie.csv')

# Cleaning the texts
import re
import nltk

nltk.download('stopwords')
    
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


corpus = []
for i in range(0, dataset.shape[0]):
    review = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 4000)
features = cv.fit_transform(corpus).toarray()

labels = dataset.iloc[:, 0].values


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = le.fit_transform(labels)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split as TTS
features_train, features_test, labels_train, labels_test = TTS(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression

model  = LogisticRegression()

model.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = model.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(labels_test, labels_pred)

score = accuracy_score(labels_test,labels_pred)

print ("Accuracy is : "+str(round(score*100, 2))+"%")