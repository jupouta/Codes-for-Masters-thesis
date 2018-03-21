import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import scipy as sp
import re
from sklearn.utils import shuffle

#%%
from base import process_corpus
resultData, originalData = process_corpus()

#%%
from sklearn.feature_extraction.text import CountVectorizer

# tokenizing and fitting to dt freq (the entire data)
countVect = CountVectorizer()

#%%
# turn the categories into numeric values
resultData['label_num'] = resultData.label.map({'Y':0, 'A':1})

X = resultData.drop(['label_num', 'label'], axis=1) # drop label from data
y = resultData.label_num


#%%
# split the data to train and test (!)
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.85)

#%%
# tokenizing and fitting with train and test
# hstacks are for concatenating BoW with extra features
feature_names = X_train.columns.tolist()[1:] # extra features with BoW
#analyzer='word', token_pattern="\S+", min_df=5
countVect = CountVectorizer(analyzer='word', token_pattern="\S+")

# the comments are for training without BoW
X_train_dtm = sp.sparse.hstack((countVect.fit_transform(X_train.message), X_train[feature_names].values), format='csr')
#X_train_dtm = X_train[feature_names].values
X_columns = countVect.get_feature_names() + X_train[feature_names].columns.tolist()
#X_columns = X_train[feature_names].columns.tolist()
X_test_dtm = sp.sparse.hstack((countVect.transform(X_test.message), X_test[feature_names].values), format='csr')
#X_test_dtm = X_test[feature_names].values

#%% Undersample training data
from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler()

X_train_resampled, y_train_resampled = rus.fit_sample(X_train_dtm, y_train)

#%% predicting
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB(alpha=1.0)

#nb.fit(X_train_dtm, y_train)
nb.fit(X_train_resampled, y_train_resampled)

y_pred_class = nb.predict(X_test_dtm)

#%% metrics, accuracy
from sklearn import metrics
from imblearn.metrics import classification_report_imbalanced
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test, y_pred_class)

print("acc (0-1) test: \n", metrics.accuracy_score(y_test, y_pred_class))
print("report test\n", metrics.classification_report(y_test, y_pred_class))
print("conf test\n", metrics.confusion_matrix(y_test, y_pred_class))
print(classification_report_imbalanced(y_test, y_pred_class))
print("\n")

#%% sample 5 & 5 per label

val_df = X_test.copy()
val_df["label"] = y_test

val_adult = val_df.loc[val_df["label"] == 1].sample(n=5)
val_young = val_df.loc[val_df["label"] == 0].sample(n=5)

val_df = val_adult.append(val_young)
val_df_X = val_df.drop(['label'], axis=1)
val_df_y = val_df.label

X_val_dtm = sp.sparse.hstack((countVect.transform(val_df_X.message), val_df_X[feature_names].values), format='csr')

y_val_pred_class = nb.predict(X_val_dtm)
y_val_pred_prob = np.around(nb.predict_proba(X_val_dtm), decimals=4)


for i in range(10):
    ser = val_df_X.iloc[i]
    indx = ser.name
    print("Formatted:", ser.message)
    print("Original:", originalData.loc[indx].message)
    print("Label:", originalData.loc[indx].label)
    print("Predicted:", y_val_pred_class[i])
    print("Prob:", y_val_pred_prob[i])
    print("")




