
#iloc and loc is important
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

#select rows by index labels
df2=df.loc[['r2']]    #select row by label
df2
df3=df.loc['r2']    #select row by label
df3
print(df.loc[['r2','r3','r6']])
print(df.loc['r1':'r5'])
print(df.loc['r1':'r5':2])

#Pandas select columns by name or index by using df[] notation
df2=df['Courses']
df2

#select multiple columns
df2=df[["Courses","Fee","Duration"]]
df2

#using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]

#Select multiple columns
df2=df.loc[:,["Courses","Fee","Duration"]]
df2

#Select random columns
df2=df.loc[:,["Courses","Fee","Discount"]]
df2

#select columns between 2 columns
df2=df.loc[:,"Fee","Discount"]
df2

#Select columns by range
df2=df.loc[:,"Duration":]
df2

#Select columns by range
#All the columns upto duration
df3=df.loc[:,:'Duration']
df3

#Select every alternate column
df4=df.loc[:,::2]
df4

##################################################################
#Pandas.DataFrame.query() by examples
#Query all rows with courses equals 'Spark'
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

df3=df.query("Courses=='Spark'")
print(df3)

##############################33
#not equal
df4=df.query("Courses !='Spark'")
print(df4)

##################################################################
#Pandas Add Column to DataFrame
import pandas as pd
technologies={
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee':[22000,25000,23000,24000,26000],
    'Discount':[0.1,0.2,0,0.5,0.1]}
df=pd.DataFrame(technologies)
print(df)

#Pandas Add Column to DataFrame
#Add new column to the DataFrame
tutors=['Ram','sham','Ghansham','Ganesh','']
df3=df.assign(TutorsAssigned=tutors)
print(df3)

#Add multiple columns to the DataFrame
MNCCompanies=['TATA','HCL','Infosys','Google','Amazon']
df4=df.assign(MNC=MNCCompanies,tutors=tutors)
df4

#################################################################
#Derive New Column from Existing Column
df=pd.DataFrame(technologies)
df3=df.assign(Discount_Percent=lambda x:x.Fee * x.Discount / 100)
df3

#################################################################
#Append column to existing Pandas DataFrame
#Add New column to the existing DataFrame

df2=pd.DataFrame(technologies)
df2["MMCCompanies"]=MNCCompanies
print(df2)

#Add new column to the specific position
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)
#################################################################
#Pandas Rename column with examples
import pandas as pd
technologies=({'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
'Fee':[20000,25000,26000,22000,24000,21000,22000],
'Duration':['30days','40days','35days','40days','60days','50days','55days']
    })
df=pd.DataFrame(technologies)
print(df)
df.columns
print(df.columns)

df3=df.rename({'Courses':'Courses_List'},axis=1)
df3=df.rename({'Courses':'Courses_List'},axis='columns')

df4.rename({'Courses':'Courses_List'},axis='columns',inplace=True)
print(df4.columns)

############################
#Rename Multiple Columns
df.rename(columns={'Courses':'Coure_list','Fee':'Course_fee','Duration':'Course_Duration'},inplace=True)
print(df.columns)