
#To check the version of pandas
import pandas as pd
pd.__version__

#Create using Constructor
#Create pandas DataFrame from list
import pandas as pd
technologies=[["Spark",20000,"30days"],
              ["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)   #list is being passed to dataframe
print(df)
print(df.dtypes)

#Dropping of columns
import pandas as pd
technologies=({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Spark","Python"],
    'Fee':[20000,25000,23000,24000,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','50days']
    })
df=pd.DataFrame(technologies)
print(df)
#Explicitly using parameter name 'labels'
df2=df.drop(labels=["Fee"],axis=1)
print(df2)
#Alternatively you can also use columns instead of labels
df2=df.drop(columns=["Fee"],axis=1)
print(df2)
#############################################################
#Drop column by index
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(technologies)
print(df)
#using inplace=True
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

#############################################################
df=pd.DataFrame(technologies)   #reinitialize --> we need dataframe in initial form

#Drop two or more columns by label name
df2=df.drop(["Courses","Fee"],axis=1)
print(df2)

#Drop two or more columns by index
df=pd.DataFrame(technologies)
df
df3=df.drop(df.columns[[0,1]],axis=1)
df3
df3=df.drop(df.columns[0],axis=1)
df3

#Drop Columns form list of Columns
df=pd.DataFrame(technologies)
df.columns     # or  print(df.columns)
lisCol=["Courses","Fee"]
df2=df.drop(lisCol,axis=1)
print(df2)

#Remove columns from DataFrame inplace
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df

########################################################
#Pandas Select Rows by index(positive/label) use of 
import pandas as pd
import numpy as np
technologies=({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee':[20000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]})
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

#df.iloc[startrow:endrow, startcolumn:endcolumn]

df=pd.DataFrame(technologies, index=row_labels)
#Below are quick example
df2=df.iloc[:,0:2]
df2
df3=df.iloc[:,:1]
df3
df4=df.iloc[:,:]
df4

#This line uses the slicing operator to get DataFrame items by index.
#The first slice[:] indicates to return all rows.
#The second slice specifies that only columns between 0 and 2 (excluding 2) should be returned

df2=df.iloc[0:2,:]
df2
#In this case the first slice [0:2] is requesting only rows 0 through lof the DataFrame.
#The second slice [:] indicates that all columns are required

#Slicing specifies rows and columns using iloc attribute
df3=df.iloc[1:2,1:3]
df3

df4=df.iloc[:,1:3]
df4
#The second operator [1:3] yields columns 1 and 3 only
#Select rows by integer index
df2=df.iloc[2]   #select row by index
df2

df2=df.iloc[[2,3,6]]   #select rows by index list
df2
df3=df.iloc[1:5]       #select rows by Interger index range
df3
df4=df.iloc[:1]        #select first row
df4
df5=df.iloc[:3]        #select first 3 rows  
df5
df6=df.iloc[-1:]       #select last row
df6
df7=df.iloc[-3:]       #select last 3 rows
df7
df8=df.iloc[::2]       #selects alternative rows
df8
