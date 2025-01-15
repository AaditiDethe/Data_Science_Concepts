
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

##################################################################
#DataFrame properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes
df.info

'''1.understanding, 2.data dictionary, 3.EDA exploring, 
4.data processing,
5.model, 6.evaluation, 7.deploy, 8.monitoring'''

##################################################################
#Accessing one column contents
df['Fee']

#Accessiong two column contents
cols=['Fee','Duration']
df[cols]
df[['Fee','Duration']]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2
df2=df[:2]   #r0 to r1
df2
df3=df[::]   #will display all rows and columns
df3
df4=df[:]    #same as above
df4
df2=df[:6]   #r0 to r5
df2

##################################################################
#accessing certain cell from column 'Duration'
df['Duration'][3]

#subtracting specific value from a column
df['Fee']=df['Fee']-500   #will reduce the price by 500
df['Fee']

#Pandas to Manipulate DataFrame
#Describe DataFrame
#Describe DataFrame for all numeric columns
df.describe()    #it will show 5 number summary
'''mean--> it is a representative number
median, standard deviation'''

##################################################################
#raname()-Renames pandas DataFrame columns
df=pd.DataFrame(technologies, index=row_labels)

#Assign new header by setting new column names.
df.columns=['A','B','C','D']
df

#Rename Column Names using rename()  method
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2
df2=df.rename(columns={'A':'c1','B':'c2'})

#################################################################
#Drop DataFrame Rows and Columns
df=pd.DataFrame(technologies,index=row_labels)

#Drop rows by labels
df1=df.drop(['r1','r2'])
df1
 #Delete Rows by position/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1

#Deletion Rows by Index Range
df1=df.drop(df.index[2:])
df1

#When you have default indexes for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0)   #it will delete row0 and row3
df1
df1=df.drop(range(0,2))     #it will delete 0 and 1
df1


