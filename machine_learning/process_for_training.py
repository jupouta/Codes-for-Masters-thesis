#%%
import numpy as np
import matplotlib
import pandas as pd
import sklearn
import random
from sklearn.utils import shuffle

#%%

data = pd.read_table("~/Google Drive/Gradu/Koodi/processing/adultProcessed.txt",
                     encoding='utf-8', names=["message", "label"], sep="\\r\\t", engine='python')
adultLabel = ["A"] * len(data)
data["label"] = adultLabel
#%%

dataYoung = pd.read_table("~/Google Drive/Gradu/Koodi/processing/youngProcessed.txt",
                          encoding='utf-8', names=["message", "label"], sep="\\r\\t", engine="python")
youngLabel = ["Y"] * len(dataYoung)
dataYoung["label"] = youngLabel
#%%
frames = [data, dataYoung]

resultData = pd.concat(frames, ignore_index=True)

#%%

resultData = shuffle(resultData)

#%% labels to category
resultData["label"] = resultData["label"].astype('category')
resultData["message"] = resultData["message"].values.astype('U')

#%%

from sklearn.feature_extraction.text import CountVectorizer


# http://scikit-learn.org/stable/datasets/index.html#external-datasets

# The most intuitive way to do so is the bags of words representation:
# 1. assign a fixed integer id to each word occurring in any document of the training set
# (for instance by building a dictionary from words to integer indices).
# 2. for each document #i, count the number of occurrences of each word w and store it in X[i, j]
# as the value of feature #j where j is the index of word w in the dictionary
# The bags of words representation implies that n_features is the number of distinct words in the corpus:
# this number is typically larger than 100,000.

# tokenizing and fitting
countVect = CountVectorizer()

countVect.fit(resultData.message.values)
simple_train_dtm = countVect.transform(resultData.message.values)
pd.DataFrame(simple_train_dtm.toarray(), columns=countVect.get_feature_names())

#countVect.fit(train) learns the vocabulary of the training data
#countVect.transform(train) uses the fitted vocabulary to build a document-term
# matrix from the training data
#countVect.transform(test) uses the fitted vocabulary to build a document-term
# matrix from the testing data (and ignores tokens it hasn't seen before)

#%%
# turn the categories into numeric values
resultData['label_num'] = resultData.label.map({'Y':0, 'A':1})

X = resultData.message
y = resultData.label_num

#%%
# split the data to train and test
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.85)



#%%
# tf-idf
# training
# predicting
# pipeline


X_train_dtm = countVect.fit_transform(X_train)
X_test_dtm = countVect.transform(X_test)

#%%
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

%time nb.fit(X_train_dtm, y_train)

y_pred_class = nb.predict(X_test_dtm)

#%%
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred_class)

metrics.confusion_matrix(y_test, y_pred_class)

# false positives (young as adult)
X_test[y_test < y_pred_class]

# false negatives (adult as young)
X_test[y_test > y_pred_class]
