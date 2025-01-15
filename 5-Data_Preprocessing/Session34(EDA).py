
############################################################

#EDA
'''Data Preprocessing'''

import pandas as pd
#let us inport dataset
df = pd.read_csv("C:/5-Data_Prep/ethnic diversity.csv")
#let us check data types of columns
df.dtypes
#salaries data type is float,let us convert into int
#df1=df.Salaries.astype(int)
df.Salaries=df.Salaries.astype(int)
df.dtypes
#now the data type of Sakaries is int 
#sSimilarly age data type must be float
#presently it is int
df.age=df.age.astype(float)
df.dtypes

########################################################
#identify the duplicates
df_new=pd.read_csv("C:/5-Data_Prep/education.csv")
duplicate=df_new.duplicated()
#Output of this function is single column
#if there is duplicate records output - True
#if there is no duplicate records output - False
#Serirs will be created 
duplicate
sum(duplicate)
#output will be 0
#Now  let us inport another dataset
df_new1=pd.read_csv("C:/5-Data_Prep/mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)

#There are three duplicate records
#row 17 is duplicate of row 2 likewise u can 3 duplicate 
#recors
#there is function called drop_duplicates()
#which will drop all the dupliacte recors
df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2)

#########################################################
#Outlier treatment
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/5-Data_Prep/ethnic diversity.csv")
#Now let us find oulier in Salaries
sns.boxplot(df.Salaries)
#there are outlier
#let us check outlier in age column
sns.boxplot(df.age)
#there are no outlier
#let us calculate IQR
IQR = df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have observed IQR in variable explorer
#no,because IQR is in capital letters
#treated as constant
IQR

#--------------------------1 Aug 2024 .......................

#but if we will try as I,IQR or iqr then it is showing
#I =df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#Iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25) 
lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
upper_limit=df.Salaries.quantile(0.75)+1.5*IQR
#now if u will check lower linit of salary it is -19446.9675
#There is negative salary so make it as 0 
#how to make it- go to varibale explorer and make it 0
lower_limit
upper_limit

########################################################################
#Trimming
import numpy as np
outlier_df=np.where(df.Salaries>upper_limit,True,
                    np.where(df.Salaries<lower_limit,True,False))
#you can check outlier of the column in variable explorer
df_trimmed=df.loc[~outlier_df]

df.shape
#0/p (310, 13)
df_trimmed.shape
#0/p (306, 13)
sns.boxplot(df_trimmed.Salaries)

########################################################
#Replacement Techniques
#Drawback of trimming techniques is we are lossing the data
df=pd.read_csv("C:/5-Data_Prep/ethnic diversity.csv")
df.describe

#record no 23 has got outliers
#map all the outlier values to upper limit 
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if the values are getting than uppper_limit
##map it to upper limit,and less than lower_limit
#map it to lower limit,if it is within the range then 
#keep it as it is
sns.boxplot(df_replaced[0])

##########################################################
'''IMP It is every time used in Data Preprocessing'''
#Winsorizer
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method= 'iqr' , 
                    tail = 'both',
                    fold = 1.5,
                    variables = ['Salaries']
                    )
#Copy Winsorizer and pastwe in Help tab of 
#top right window , study the method 
#

df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])

#################################################################3

#---------------------------2 August 2024..........................
#Zerovarience and near zero varience
#if there is no varience in feature, then ML model 
#will not be intelligent
import pandas as pd
df=pd.read_csv("C:/5-Data_Prep/ethnic diversity.csv")
df.var() #error
#here EmpId and ZIP is nominal data
#Salary has 4.441953e+08 is 4441953000
#not close to zero
df.info()
df.Salaries.var()==0
df.var(axis=0)==0 #error

##################################################################
import pandas as pd
import numpy as np
df=pd.read_csv("C:/5-Data_Prep/modified ethnic.csv")
#check for null values
df.isna().sum()
#Output: 
#Position            43
#State               35
#Sex                 34
#MaritalDesc         29
#CitizenDesc         27
#EmploymentStatus    32
#Department          18
#Salaries            32
#age                 35
#Race                25
#dtype: int64
##########################################

#create imputer that creates NaN values
#mean and median is used for numeric data
#mode is used for discrete data(position,sex,,MaritalDes)
from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
#check the dataframe
df['Salaries'] = pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
#check the dataframe
df['Salaries'].isna().sum()
'''0/p :- 0 '''

##########################################
#median imputer [used when their are outlier here in age outlier are present no in salaries]
from sklearn.impute import SimpleImputer
median_imputer=SimpleImputer(missing_values=np.nan,strategy='median')
#check the dataframe
df['age'] = pd.DataFrame(median_imputer.fit_transform(df[['age']]))
#check the dataframe
df['age'].isna().sum() 
'''0/p :- 0 '''
#########################################################
from sklearn.impute import SimpleImputer
mode_imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
#check the dataframe
df['Sex'] = pd.DataFrame(mode_imputer.fit_transform(df[['Sex']]))
df['Sex'].isna().sum() 
#o/p:- 0
df['MaritalDesc']= pd.DataFrame(mode_imputer.fit_transform(df[['MaritalDesc']]))
df['MaritalDesc'].isna().sum()
#o/p :- 0

###############################################3
#install anaconda prompt[pip install imbalanced-learn scikit-learn]
'''IMP'''
# pip install imbalanced-learn scikit-learn
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE

#Step 1: Generate an imbalanced dataset
X,y = make_classification(n_samples=1000, n_features=20,n_informative=2,n_redundant=10,n_clusters_per_class=1,weights=[0.99],flip_y=0,random_state=1)

'''
Parameters -

n_samples=1000:
    the total number of samples (data points) to generate. 
    here 1000 sample will be created
n_features=20:
    The total number of features(columns) in the daset.
    Each sample will have 20 features
       
n_informative=2:
    the number of informative features.
    these features are useful for oredicting the target variables
    
n_redundant=10:
    the number of radundant features.
    tjese featres are generated as random linear combinations of the 
    
n_clusters_per_class=1:
    the number of clusters per class.
     each class will have one cluster of points
     this parameter is useful for contrlling the overlap between
    
weight=[0.99]:the propogation of samples assigne to each class,
Here 99%of samples will bringto one class,
creating a sifnificant class imbalanced the remaining 1% will be
    
    
flip_y=0: The fraction of samle whose class is randomly fliped
    
random_state = 1:
    the seed used by the random number generator.this 
    
'''

#Show the original classs distribution
print("Original class distribution:",np.bincount(y))

#Step :2 Apply SMOTE to balance the dataset
smote = SMOTE(random_state=42)
X_res,y_res=smote.fit_resample(X,y)

#Show the new class distribution after applying SMOTE
print("Resampled class distribtion",np.bincount(y_res))


#Show the original class distribution
print(f"Original class distribution:{np.bincount(y)}")
from sklearn.model_selection import train_test_split
#Step-2: split the data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

#Step-3: Apply SMOTE to balance the training dataset
smote=SMOTE(random_state=42)
X_train_res, y_train_res=smote.fit_resample(X_train,y_train)

#Show the new class distribution after applying SMOTE
print(f"Resampled class distribution:{np.bincount(y_train_res)}")

from sklearn.ensemble import RandomForestClassifier
#Step-4: Train  classifier on the balanced data set
clf=RandomForestClassifier(random_state=42)
clf.fit(X_train_res,y_train_res)

#Step: Evaluate the classifier on the test set
y_pred=clf.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test,y_pred))

##############################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Generate a sample dataset
np.random.seed(0)
data=np.random.exponential(scale=2.0,size=1000)
df=pd.DataFrame(data,columns=['Value'])

#Perform log transformation
df['LogValue']=np.log(df['Value'])

#Plot the original and the log-transformed data
fig,axes=plt.subplots(1,2,figsize=(12,6))

#Original data    
axes[0].hist(df['Value'],bins=30,color='blue',alpha=0.7)
axes[0].set_title('Original Data')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Frequency')


#Log-Transformed data
axes[1].hist(df['LogValue'],bins=30,color='green',alpha=0.7)
axes[1].set_title('Log-transformed Data')
axes[1].set_xlabel('Log(Value)')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

#   

