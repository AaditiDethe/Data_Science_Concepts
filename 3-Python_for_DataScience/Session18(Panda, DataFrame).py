
#Pandas Shuffle DataFrame Rows
import pandas as pd
technologies=({ 
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]})
df=pd.DataFrame(technologies)
print(df)

#shuffle the DataFrame rows and return all rows
df1=df.sample(frac=1)
df1

df2=df.sample(frac=0)
df2    #output --> Empty DataFrame

#Create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)

#Drop shuffle Index
df1=df.sample(frac=1).reset_index(drop=True)
df1

##################################################################
#Join
import pandas as pd
technologies={
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days']}
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)

technologies2={
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]}
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)

#pandas join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3) #matching rows with nan value are displayed

#pandas Inner Join DataFrames
df4=df1.join(df2,lsuffix="_left",rsuffix="_right",how="inner")
print(df4)   #only matching rows are displayed

#Pandas Right Join DataFrames
df5=df1.join(df2,lsuffix="_left",rsuffix="_right",how="right")
df5

#Pandas Left Join DataFrames
df6=df1.join(df2,lsuffix="_left",rsuffix="_right",how="left")
df6

##################################################################
#Pandas Merge DataFrames
import pandas as pd
technologies={
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days']}
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)

technologies2={
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]}
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)

#using pandas.merge()
df3=pd.merge(df1,df2)   #does not repeat column, display matching rows
df3

#Usind DataFrame.merge()
df4=df1.merge(df2)
df4

df5=df2.merge(df1)
df5

##################################################################
#Use pandas.concat() to concat 2 DataFrame
#1 table will concat vertically
import pandas as pd
df=pd.DataFrame({
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,24000]})

df1=pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","Java"],
'Fee':[25000,25200,24500,24900]})

#Using pandas.concat() to concat 2 DataFrames
data=[df,df1]            #1st df and then df1 concat(add at last of df)
df2=pd.concat(data)
df2

data=[df1,df]     #1st df1 and then df concat(add at last of df1)
df3=pd.concat(data)
df3

#Concatenate Multiple DataFrames using pandas.concat()
import pandas as pd
df=pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':['20000','25000','22000','24000']})

df1=pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                  'Fee':['25000','25200','24500','24900']})

df2=pd.DataFrame({'Duration':["30days","40days","35days","60days","55days"],
                  'Discount':[1000,2300,2500,2000,3000]})

#Appending multiple DataFrame
df3=pd.concat([df,df1,df2])
df3

