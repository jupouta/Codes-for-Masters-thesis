import numpy as np
import matplotlib
import pandas as pd
from sklearn.utils import shuffle

#%%
from base import process_corpus
resultData = process_corpus()
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

# tokenizing and fitting to dt freq (the entire data)
countVect = CountVectorizer()

countVect.fit(resultData.message.values)
simple_train_dtm = countVect.transform(resultData.message.values)
#%%
# visualization(s) of the most frequent features in bag of word
bow_df = pd.DataFrame(simple_train_dtm.toarray(), columns=countVect.get_feature_names())
word_freq_cumsum = bow_df.sum(axis=0)
word_freq_top50 = word_freq_cumsum.sort_values(ascending=False).head(50).plot(kind="bar", title="Les 50 mots les plus utilisés parmi les jeunes et les adultes")
word_freq_top100 = word_freq_cumsum.sort_values(ascending=False).head(100).plot(kind="bar", title="Les 100 mots les plus utilisés parmi les jeunes et les adultes")

word_freq_least20 = word_freq_cumsum.sort_values(ascending=False).tail(20).plot(kind="bar", title="Les 20 mots les moins utilisés parmi les jeunes et les adultes")
word_freq_least100 = word_freq_cumsum.sort_values(ascending=False).tail(100).plot(kind="bar", title="Les 100 mots les moins utilisés parmi les jeunes et les adultes")

#%% young
countVectY = CountVectorizer()
countVectY.fit(resultData.message[resultData.label=="Y"].values)
simple_train_dtm_Y = countVectY.transform(resultData.message[resultData.label=="Y"].values)

bow_df_y = pd.DataFrame(simple_train_dtm_Y.toarray(), columns=countVectY.get_feature_names())
word_freq_cumsum_y = bow_df_y.sum(axis=0)
word_freq_top20Y = word_freq_cumsum_y.sort_values(ascending=False).head(20).plot(kind="bar", title="Les 20 mots les plus utilisés parmi les jeunes")
word_freq_top100Y = word_freq_cumsum_y.sort_values(ascending=False).head(100).plot(kind="bar", title="Les 100 mots les plus utilisés parmi les jeunes")

#%% adults

countVectA = CountVectorizer()
countVectA.fit(resultData.message[resultData.label=="A"].values)
simple_train_dtm_A = countVectA.transform(resultData.message[resultData.label=="A"].values)

bow_df_a = pd.DataFrame(simple_train_dtm_A.toarray(), columns=countVectA.get_feature_names())
word_freq_cumsum_a = bow_df_a.sum(axis=0)
word_freq_top20A = word_freq_cumsum_a.sort_values(ascending=False).head(20).plot(kind="bar", title="Les 20 mots les plus utilisés parmi les adultes")
word_freq_top100A = word_freq_cumsum_a.sort_values(ascending=False).head(100).plot(kind="bar", title="Les 100 mots les plus utilisés parmi les adultes")

#%% word_freq differences

word_freq_cumsum.sort_values(ascending=False).head(50) / sum(word_freq_cumsum)
sum(word_freq_cumsum.sort_values(ascending=False).head(20) / sum(word_freq_cumsum))

# relative freq for adults
word_freq_cumsum_a.sort_values(ascending=False).head(50) / sum(word_freq_cumsum_a)

rel_freq_y = word_freq_cumsum_y / sum(word_freq_cumsum_y)
rel_freq_a = word_freq_cumsum_a / sum(word_freq_cumsum_a)

abs((rel_freq_y - rel_freq_a)).sort_values(ascending=False)
