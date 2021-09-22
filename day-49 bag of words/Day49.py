import pandas as pd

df =  pd.read_csv('balanced_reviews.csv')

df.shape

df.columns

df.sample(10)

df['reviewText'][0]

df['overall'].value_counts()

df.isnull().any(axis = 0)

df.dropna(inplace =  True)

df = df [df['overall'] != 3]

import numpy as np

df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)

#NLP
#reviewText - feature - df['reviewText']
#Positivity - label - df['Positivity']

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(df['reviewText'], df['Positivity'], random_state = 42 )



from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer().fit(features_train) #it will collect all the unique words

len(vect.get_feature_names()) #number of unique words indentified 


vect.get_feature_names()[10000:10010]


features_train_vectorized = vect.transform(features_train)
















