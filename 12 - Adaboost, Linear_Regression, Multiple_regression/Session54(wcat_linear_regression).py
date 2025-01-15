
# OLS - Ordinary Least Square

import pandas as pd
import numpy as np
import seaborn as sns
wcat = pd.read_csv("C:/14_Linear_Regression/wc-at.csv")
wcat.info()
wcat.describe()

# Average waist is 91.90 and min is 63.50 and max is 121
# Average AT is 101.89 and min is 11.44 and max is 253

import matplotlib.pyplot as plt
plt.bar(height = wcat.AT,x=np.arange(1,110,1))
sns.distplot(wcat.AT)
# Data is normal but right skewed
plt.boxplot(wcat.AT)
# No outliers but right skewed
plt.bar(height=wcat.Waist,x=np.arange(1,110,1))
sns.displot(wcat.Waist)
# Data is normal bimodal
plt.boxplot(wcat.Waist)
# No outliers but right skewed
#############################

#Bivariant analysis
plt.scatter(x=wcat.Waist,y=wcat.AT)
# Data is linearly scattered, direction positive, strenght:poor
# Now let us check the correlation coefficient
np.corrcoef(wcat.Waist,wcat.AT)

# The correlation coefficient is 0.8185<0.85 hence the correlation 
#is moderate
# Let us check the direction of correlation
cov_output = np.cov(wcat.Waist,wcat.AT)[0,1]
cov_output
#635.91 it is positive means correlation will be positive
##############################################################

# let us apply to various models and check the feasibility
import statsmodels.formula.api as smf
# first simple linear model
model=smf.ols('AT~Waist',data=wcat).fit()
# Y is AT and X is waist
model.summary()
# R-squared = 0.67<0.85, there is scope of improvement
# p=00<0.05 hence acceptable
# bita-0 = -215.98
# bita-1 = 3.45
pred1 = model.predict(pd.DataFrame(wcat.Waist))
pred1

######################################
# Regression line
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred1,'r')
plt.legend(['Predicted line','Observed data'])
plt.show()
######################################

#error calculations
res1 = wcat.AT-pred1
np.mean(res1)
res_sqr1 = res1*res1
mse1 = np.mean(res_sqr1)
rmse1 = np.sqrt(mse1)
rmse1
# 32.76



#######################################
# let us try another model
#x=log(Waist)
plt.scatter(x=np.log(wcat.Waist),y=wcat.AT)
# Data is linearly scattered, direction positive, strength:poor
# Now let us check the correlation coefficient
np.corrcoef(np.log(wcat.Waist),wcat.AT)
# The correlation coefficient is 0.8185<0.85 hence the correlation
# r = 0.8217
model2 = smf.ols('AT~np.log(Waist)',data=wcat).fit()
# Y is AT and X = log(Waist)
model2.summary()
# R-squared = 0.675<0.85, there is scope of improvement
# p=00<0.05 hence acceptable
# bita-0 = -1328.3420
# bita-1 = np.log(Waist) 317.1356
pred2 = model2.predict(pd.DataFrame(wcat.Waist))
pred2
##########################################

# Regression line
plt.scatter(np.log(wcat.Waist),wcat.AT)
plt.plot(np.log(wcat.Waist),pred2,'r')
plt.legend(['Predicted line','Observed data_model2'])
plt.show()
#########################

# error calculations
res2 = wcat.AT-pred2
np.mean(res2)
res_sqr2 = res2*res2
mse2 = np.mean(res_sqr2)
rmse2 = np.sqrt(mse2)
rmse2
# 32.49
# There is no significant changeas r=0.821. RSquare = 0.675 and RMSE = 32.49

#############################################
# Hence let us try another model

# Now let us make logY and X as is
plt.scatter(x=(wcat.Waist),y=np.log(wcat.AT))
# Data is linearly scattered, direction positive, strenght: poor

# Now let us check the correleation coefficient
np.corrcoef(wcat.Waist, np.log(wcat.AT))
# The correlation coefficient is 0.8185<0.85 hence the correlation is moderate
# r = 0.8409
model3=smf.ols('np.log(AT)~Waist',data=wcat).fit()
# Y is log(AT) and X=Waist
model3.summary()
# R-sqarred = 0.707<0.85, there is scope of improvement
# p  =0.002<0.05 hence acceptable
# bita-0 = 0.7410
# bita-1 = 0.0403

pred3 = model3.predict(pd.DataFrame(wcat.Waist))
pred3_at = np.exp(pred3)
pred3_at
###############################
# Regression line
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist,pred3,'r')
plt.legend(['Predicted line','Observed data_model3'])
plt.show()
##############################

# error calculations
res3 = wcat.AT-pred3_at
res_sqr3 = res3*res3
mse3 = np.mean(res_sqr3)
rmse3 = np.sqrt(mse3)
rmse3
#38.52
# There is no significant change as r=0.8409, R-sqarred=0.707 and RMSE=38.52

#####################################################
# Now let us try another model

# Now let us make Y=log(AT) and X=Waist, X*X=Waist.Waist
# polynomial model
# Here r cannot be calculated
model4 = smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
# Y is log(AT) and X=Waist
model4.summary()
# R-sqarred = 0.779<0.85, there is scope of improvement
# p  =0.000<0.05 hence acceptable
# bita-0 = -7.8241
# bita-1 = 0.2289

pred4 = model4.predict(pd.DataFrame(wcat.Waist))
pred4
pred4_at = np.exp(pred4)
pred4_at
###############################
# Regression line
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist,pred4,'r')
plt.legend(['Predicted line','Observed data_model3'])
plt.show()
##############################

# error calculations
res4 = wcat.AT-pred4_at
res_sqr4 = res4*res4
mse4 = np.mean(res_sqr4)
rmse4 = np.sqrt(mse4)
rmse4
#32.24

# We have to generalize the best model
from sklearn.model_selection import train_test_split
train,test = train_test_split(wcat,test_size=0.2)
plt.scatter(train.Waist,np.log(train.AT))
plt.scatter(test.Waist,np.log(test.AT))
final_model=smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
# Y is log(AT) and X=Waist
final_model.summary()
# R-sqarred = 0.779<0.85, there is scope of improvement
# p = 0.000<0.05 hence acceptable
# bita-0 = -7.8241
# bita-1 = 0.2289

test_pred = final_model.predict(pd.DataFrame(test))
test_pred_at = np.exp(test_pred)
test_pred_at
###############################################

train_pred = final_model.predict(pd.DataFrame(train))
train_pred_at = np.exp(train_pred)
train_pred_at

##########################################3
# Evaluation on test data
test_res = test.AT-test_pred_at
test_sqr = test_res*test_res
test_mse = np.mean(test_sqr)
test_rmse = np.sqrt(test_mse)
test_rmse

#Evaluation in train data
train_res = train.AT-train_pred_at
train_sqr = train_res*train_res
train_mse = np.mean(train_sqr)
train_rmse = np.sqrt(train_mse)
train_rmse
########################################

#Evaluation in train data
#test_rmse>train_rmse

# Evaluation in test data


