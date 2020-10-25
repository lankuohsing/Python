# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 22:15:14 2020

@author: lankuohsing
"""
from sklearn.feature_extraction.text import CountVectorizer
# In[]
vectorizer = CountVectorizer()
# In[]
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
X = vectorizer.fit_transform(corpus)

# In[]
print(vectorizer.get_feature_names())
# In[]
print(X.toarray())
# In[]
print(vectorizer.vocabulary_.get('document'))

# In[]
print(vectorizer.transform(['Something completely new.']).toarray())
print(vectorizer.transform(['This is the first document.']).toarray())
# In[]
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2),
                                    token_pattern=r'\b\w+\b', min_df=1)
# In[]
X_2 = bigram_vectorizer.fit_transform(corpus).toarray()
print(X_2)
# In[]
feature_index = bigram_vectorizer.vocabulary_.get('is this')
print(X_2[:, feature_index])