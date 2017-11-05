# -*- coding: utf-8 -*-

%matplotlib inline
import sys
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from __future__ import print_function

# turn of data table rendering
pd.set_option('display.notebook_repr_html', False)
sns.set_palette(['#00A99D', '#F5CA0C', '#B6129F', '#76620C', '#095C57'])
sys.version

#%%  We create 40 separable points
np.random.seed(40)
X=np.r_[np.random.randn(20,2) - [2,2], np.random.randn(20,2)+[2,2]]
Y = [0] * 20 + [1] * 20

#%% Fit SVM with linear kernel
clf=SVC(kernel='linear')
clf.fit(X,Y)

# get seperating hyperplane 
w=clf.coef_[0]
a=-w[0]/w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (clf.intercept_[0]) / w[1]


#Plot the parallels to the separating hyperplane that pass through the
# support vectors
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

# Plot the line, the points, and the nearest vectors to the plane
plt.plot(xx, yy, 'k-', color='#00A99D')
plt.plot(xx, yy_down, 'k--', color='gray')
plt.plot(xx, yy_up, 'k--', color='gray')

# Plot the support vectors in yellow
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
            s=200, color='#F5CA0C')
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='gray', s=60)
plt.show()


#%% Kernel functions 
df = pd.read_csv('Data/tweets.csv')
df.screen_name.value_counts() # count the values

# Show arbitrary datapoint
df.screen_name[331], df.tweet[331]

# Shuffle the data
def shuffle(data,n):
    ind = data.index
    for i in range(n):
        sampler=np.random.permutation(data.shape[0])
        new_vals=data.take(sampler).values
        data=pd.DataFrame(new_vals, index=ind)
        return data
    
df = shuffle(df, 1)
df.columns = ['screen_name', 'tweet']
df.head()

# Create a training set (3/4 of the data)
train_n=300
train_features=df['tweet'][:train_n]
train_labels=df['screen_name'][:train_n]
train_features.count()

# Create a test set (1/4 of the data)
test_features=df['tweet'][train_n:]
test_labels=df['screen_name'][train_n:]
test_features.count()

#%% TF-IDF Feature Vectors 
# In order to perform machine learning on text documents, we first 
# need to turn the text content into numerical features.
count_vectorizer = CountVectorizer()
train_counts = count_vectorizer.fit_transform(train_features)
train_counts.shape

# Transform to Term Frequencies - Inverse Document Frequencies
tfidf_transformer = TfidfTransformer(use_idf=False)
tfidf_transformer.fit(train_counts)

train_tfidf = tfidf_transformer.transform(train_counts)
train_tfidf.shape

# Create a TF-IDF for the test data
test_counts = count_vectorizer.transform(test_features)
test_tfidf = tfidf_transformer.transform(test_counts)
test_tfidf.shape

#%% Training the SVM Classifier
Mdl = SVC(kernel="linear")
Mdl.fit(train_tfidf, train_labels)

# Predict with the test data
pred = Mdl.predict(test_tfidf)
pred[:11]

# Plot the accuracy of the model
sns.barplot(test_labels == pred)
plt.show()

# Calculate the accuracy
accuracy = accuracy_score(pred, test_labels)
accuracy