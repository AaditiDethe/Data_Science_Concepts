# One-hot-encoding

import pandas as pd
df=pd.read_csv('C:/8-text_mining/text_mining\homeprices.csv')
df.head()

dummies=pd.get_dummies(df.town)
dummies


merged=pd.concat([df,dummies],axis='columns')
merged

final=merged.drop(['town'],axis='columns')
final

'''Dummy Variable Trap

When you can derive one variable from other variables, they are known to be multi-colinear. Here if you know values of california and georgia then you can easily infer value of new jersey state, i.e. california=0 and georgia=0. There for these state variables are called to be multi-colinear. In this situation linear regression won't work as expected. Hence you need to drop one column. NOTE: sklearn library takes care of dummy variable trap hence even if you don't drop one of the state columns it is going to work, however we should make a habit of taking care of dummy variable trap ou are using is not handling this for you'''


final = final.drop(['west windsor'],axis='columns')
final

X=final.drop('price',axis='columns')
X

y=final.price

from sklearn.linear_model import LinearRegression
model = LinearRegression()    

model.fit(X,y)               #train the model              #Define the model

model.predict(X)

model.score(X,y)

model.predict([[3400,0,0]])    #3400 sqr ft in home in west windsor"


model.predict([[2800,0,1]])    #2800 sqr ft in home in robinsville"

#Using sklearn OneHOtEncoder
#First step is to use label encoder to convert town names into numbers

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

dfle=df
dfle.town=le.fit_transform(dfle.town)
dfle

x=dfle[['town','area']].values
x

y=dfle.price
y

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([("town",OneHotEncoder(),[0])],remainder='passthrough')
x=ct.fit_transform(x)
x

#The code creates a column transformer that one hot encodes the first column
#index 0 of the dataset and leaves the remaining columns unchanged(passthrough)
#this is useful when you have a mix of categorical and numerical features in your dataset and what to apply specific
#transformation  only to certain columns while keeping others as they are

x=x[:,1:]
x
model.fit(x,y)

model.predict([[0,1,3400]])   #3400 sq ft home in Robinville

model.predict([[1,0,2800]])  #2800 sq ft home in Wind Windsor

model.score(x,y)