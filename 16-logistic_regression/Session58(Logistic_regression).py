
############################# Logistic Regression ##########################

# import important libraries:
import pandas as pd
from matplotlib import pyplot as plt

# load the data set:
df = pd.read_csv("C:/15-logistic_regression/insurance_data.csv")
df.head()

# plot:
plt.scatter(df.age,df.bought_insurance, marker='+', color='red')

# Train the data:
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, train_size = 0.8)
X_test

# Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)

y_predicted = model.predict(X_test)
model.predict_proba(X_test)

model.score(X_test, y_test)
y_predicted

X_test

#model.coef_ indicates value of m  in y=mx+b equation
model.coef_

#model.intercept_ indicates value of b  in y=mx+b equation
model.intercept_

# Lets define sigmoid function now and do the math with hand
import math
def sigmoid(x):
    return 1/(1+math.exp(-x))


def prediction_function(age):
    z = 0.042* age-1.53
    y = sigmoid(z)
    return y

age = 35
prediction_function(age)
# Output : 0.4850044983805899

# 0.485 is less than 0.5 which means person with 35 age will not buy insurance.

age = 43
prediction_function(age)
# Output : 0.568565299077705

# 0.568 is greater than 0.5 which means person with 43 age will buy insurance.