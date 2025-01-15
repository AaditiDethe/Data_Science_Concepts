
# Decision Tree Classifier
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
data = pd.read_csv("C:/11_KNN/Decision_Tree/credits.csv")

data.head()
# Data preparation
# check for null values

data.isnull().sum()
data.dropna()
data.columns

# There are 9 columns having non numeric values, let us treat them 
# There is one column called phone whcih is not useful, let us drop
data = data.drop(["phone"], axis = 1)

# Now there are 16 columns

lb = LabelEncoder()
data["Checking_balance"]=lb.fit_transform(data["checking_balance"])
data["credit_history"]=lb.fit_transform(data["credit_history"])
data["purpose"]=lb.fit_transform(data["purpose"])
data["savings_balance"]=lb.fit_transform(data["savings_balance"])
data["employment_duration"]=lb.fit_transform(data["employment_duration"])
data["other_credit"]=lb.fit_transform(data["other_credit"])
data["housing"]=lb.fit_transform(data["housing"])
data["job"]=lb.fit_transform(data["job"])

# Check for non-numeric columns
non_numeric_cols = data.select_dtypes(include=["object"]).columns
print(non_numeric_cols)
data["checking_balance"]=lb.fit_transform(data["checking_balance"])
data["default"]=lb.fit_transform(data["default"])

# Now let us check how many unique values are there in target column
data["default"].unique()
data["default"].value_counts()

# Now we want to split the tree, we need all feature columns
colnames = list(data.columns)

# Now let us assign these columns to variables predictor
predictors = colnames[:15]
target = colnames[15]

# Splitting data into training and testing data set
from sklearn.model_selection import train_test_split
train, test = train_test_split(data, test_size = 0.3)

from sklearn.tree import DecisionTreeClassifier as DT

help(DT)
model = DT(criterion = 'entropy')
model.fit(train[predictors], train[target])

# Prediction on test data
preds = model.predict(test[predictors])
pd.crosstab(test[target], preds, rownames=['Actual'], colnames = ['Predictions'])

np.mean(preds == test[target])  # Test data accuracy

# Prediction on train data
preds = model.predict(train[predictors])
pd.crosstab(train[target], preds, rownames = ['Actual'], colnames = ['Predictions'])

np.mean(preds == train[target])  # Train Data Accuracy

#######################################################################

# New problem:
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DT

# Load the dataset
data = pd.read_csv("C:/11_KNN/Decision_Tree/salaries.csv")

# Data preparation
# Encode categorical features
lb = LabelEncoder()
data['company'] = lb.fit_transform(data['company'])
data['job'] = lb.fit_transform(data['job'])
data['degree'] = lb.fit_transform(data['degree'])

# Define predictors and target
predictors = ['company', 'job', 'degree']
target = 'salary_more_than_100k'

# Split data into training and testing sets
train, test = train_test_split(data, test_size=0.3, random_state=42)

# Build and train the Decision Tree model
model = DT(criterion='entropy')
model.fit(train[predictors], train[target])

# Prediction on test data
preds_test = model.predict(test[predictors])
test_accuracy = np.mean(preds_test == test[target])

# Prediction on train data
preds_train = model.predict(train[predictors])
train_accuracy = np.mean(preds_train == train[target])

# Print the accuracy results
print("Test Data Accuracy:", test_accuracy)
print("Train Data Accuracy:", train_accuracy)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=predictors, class_names=['<=100K', '>100K'], filled=True, rounded=True, fontsize=12)
plt.title("Decision Tree for Salary Prediction")
plt.show()
