# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:02:19 2018

@author: l00467141
"""
# In[]
import pandas as pd
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
# In[]
iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 2, 4], 'gamma':[0.125, 0.25, 0.5 ,1, 2, 4]}
svr = svm.SVC()
clf = GridSearchCV(svr, parameters)
clf.fit(iris.data, iris.target)
# In[]
cv_result = pd.DataFrame.from_dict(clf.cv_results_)
with open('cv_result.csv','w') as f:
    cv_result.to_csv(f)
    
print('The parameters of the best model are: ')
print(clf.best_params_)

y_pred = clf.predict(iris.data)
# In[]
print("result:",classification_report(y_true=iris.target, y_pred=y_pred))