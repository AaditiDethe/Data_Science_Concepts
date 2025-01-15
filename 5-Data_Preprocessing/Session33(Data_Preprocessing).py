
import pandas as pd
#let us import dataset
df=pd.read_csv("C:/5-data_prep/ethnic diversity.csv")
#let us check data types of columns
df.dtypes
#salaries datatype is float, let us convert into int
df.Salaries=df.Salaries.astype(int)
df.dtypes
#now the data type of Salaries is int

#Similarly age data type must be float, presently it is int
df.age=df.age.astype(float)
df.dtypes

##################################################################
#Identify the duplicates
df_new=pd.read_csv("C:/5-data_prep/education.csv")
duplicate=df_new.duplicated()
duplicate
'''Output of this function is single column. If there is duplicate
records output -True. If there is no duplicate records output -False
Series will be created.'''
sum(duplicate)
#Output will be zero as there are no duplicate records

#Now let us import another dataset
df_new1=pd.read_csv("C:/5-data_prep/mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)  #Output will be 3
'''There are 3 duplicate records. Row 17 is duplicated of row 2'''

#There is function called drop_duplicates()
'''It will drop all the duplicate records'''
df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2) # Output --> 0

######################################################################

#Outliers treatment
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/5-data_prep/ethnic diversity.csv")
#Now let us find outliers in Salaries
sns.boxplot(df.Salaries)
#There are outliers
#Let us check outliers in age column
sns.boxplot(df.age)
#There are no outliers
#Let us calculate IQR
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have observed IQR in variable explorer
#no,because IQR is in capital letters
#treated as constant
IQR
#but if we will try as I, IQR or iqr or Iqr then it is showing
#I=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#Iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
upper_limit=df.Salaries.quantile(0.75)+1.5*IQR
#Now it you will check the lower limit of salary, it is -19446.9675
#There is negative salary, so make it as 0
#How to make it --> go to variable explorer and make it 0
lower_limit
upper_limit
#Upper limit is 93992.8125

###################################################################

#Trimming 
'''Trimming should be the last method to remove outliers'''
import numpy as np
outliers_df=np.where(df.Salaries>upper_limit,True,np.where(df.Salaries<lower_limit,True,False))
#you can check outliers_df column in variable explorer

df_trimmed=df.loc[~outliers_df]
df.shape
#(310,13)
#After trimming
df_trimmed.shape
#(306, 13)   #outliers are removed after trimming --> 4 outliers are removed

#Now I want to recomform that the outliers are removed or not?
sns.boxplot(df_trimmed.Salaries)

#####################################################################

#Replacement Technique
#Drawback of trimming --> losing the data
import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv("C:/5-data_prep/ethnic diversity.csv")
df.describe() 

#record no.23 has got outliers
#map all the outlier value to upper limit
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,
            np.where(df.Salaries<lower_limit,lower_limit,
            df.Salaries)))
'''If the values are greater than upper limit --> map it to upper_limit,
and less than lower limit map it to lower limit, it it is within the range
then keep it as it is.'''
sns.boxplot(df_replaced[0])

#######################################################################

#Winsorizer
import pandas as pd
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Salaries']
                  )
#Copy Winsorizer and paste in Help tab of top right window, study the method

df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])

import pandas as pd
print(pd.__version__)
