
#DataFrame Features
'''2-D datastructure and it is immutable, supports named rows and
column. Supports heterogeneous collection of data. DataFrame labeled
axes(rows and columns)
Installing pandas:
    step-1: go to anaconda navigator
    step-2: select environment lab
    step-3: by default it will be base terminal
    step-4: on base terminal-pip install pandas  or  conda install 
    pandas
    
 other method:
     on base terminal write--> conda install -c anaconda pandas'''

##################################################################
#Creating using Constructor
#create pandas DataFrame from list
import pandas as pd
technologies=[["Spark",20000,"30days"],
              ["Pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)
'''Since we have not given labels to columns and indexes, DataFrame
by default assigns  incremental sequence numbers as labels to both
rows and columns, these are called Index.'''
#Add column and row to the DataFrame
import pandas as pd
technologies=[["Spark",20000,"30days"],
              ["Pandas",20000,"40days"]]
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
df.dtypes

##################################################################
'''You can also assign custom datatypes to columns.Set custom 
types to DataFrame'''
import pandas as pd
technologies={
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','35days','34days','50days','60days','45days','44days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df=pd.DataFrame(technologies)
print(df)
print(df.dtypes)
#Convert all types to best possible types
df2=df.convert_dtypes()   #it is a function
print(df2.dtypes)
#Change all columns to the same type
df=df.astype(str)
print(df.dtypes)
#Change Type For One or Multiple Columns
df=df.astype({"Fee":int,"Discount":float})  
print(df.dtypes)
#Convert data type for All Columns in a List
import pandas as pd
technologies={
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','35days','34days','50days','60days','45days','44days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

#Ignores error
df=df.astype({'Courses':int},errors='ignore')  #will not give error 
#and not convert object into int
df.dtypes

#Generates error
df=df.astype({'Courses':int},errors='raise')

#Converts feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df['Discount']=pd.to_numeric(df['Discount'])
df.dtypes

##################################################################
import pandas as pd
technologies={
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','35days','34days','50days','60days','45days','44days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df=pd.DataFrame(technologies)
df
df.to_csv('data_file.csv')
df=pd.read_csv('data_file.csv')

#################################################################
#Pandas DataFrame - Basic operations
#create DataFrame with None/Null to work with examples
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
