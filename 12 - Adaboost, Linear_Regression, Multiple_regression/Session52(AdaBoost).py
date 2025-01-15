# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:45:09 2024

@author: aadit
"""

# import necessary packages
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')
# read csv file
loan_data = pd.read_csv("C:/13-AdaBoost/income.csv")
loan_data.columns
loan_data.head()

# Let us split the data in input and output
X = loan_data.iloc[:,0:6]
y = loan_data.iloc[:,6]

# Split the dataset
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size = 0.2)

# Create AdaBoost Classifier
ada_model = AdaBoostClassifier(n_estimators=100, learning_rate=1)
#n_estimators =number of weak learners
#learning rate, it contributes weights of weak learners, bydefault
# Train the model
model=ada_model.fit(X_train,y_train)
# predict the results
y_pred = model.predict(X_test)
print("accuracy", metrics.accuracy_score(y_test, y_pred))

# let us try for another base model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

#here base model is changed
Ada_model = AdaBoostClassifier(n_estimators = 50,estimator=lr,learning_rate=1)  
# instead of base_estimator write estimator
model = ada_model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("accuracy",metrics.accuracy_score(y_test,y_pred))
