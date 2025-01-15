
#Quick Examples of get the number of rows in DataFrame
import pandas as pd
technologies=({'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
'Fee':[20000,25000,26000,22000,24000,21000,22000],
'Duration':['30days','40days','35days','40days','60days','50days','55days']
    })
df=pd.DataFrame(technologies)
print(df)
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count

###################################################################
df=pd.DataFrame(technologies)
row_count=df.shape[0] #return number of rows
row_count
col_count=df.shape[1] #return number of columns
print(row_count)
print(col_count)
col_count1=df.shape[0] # 0 for rows and 1 for column
col_count1             #it will display no of rows

##################################################################
#Below are quick examples
#Using DataFrame.apply() to apply function add column
import pandas as pd
import numpy as np
data={'A':[1,2,3],
      'B':[4,5,6],
      'C':[7,8,9]}
df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
df4=((df.A).apply(add_3))
df4

def mul_4(x):
    return x*4
df3=df.apply(mul_4)
df3
print(((df.C).apply(mul_4)))

##################################################################
#Using apply function single column
import pandas as pd
import numpy as np
data={'A':[1,2,3],
      'B':[4,5,6],
      'C':[7,8,9]}
df=pd.DataFrame(data)
print(df)
def add_4(x):
    return x+4
df['B']=df['B'].apply(add_4)
df['B']

#Apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_4)
df

#apply a lambda function to each column
df2=df.apply(lambda x:x+10)
df2

#############################################################
#Apply Lambda Function to single column
#Using DataFrame.apply() and lambda function
df['A']=df['A'].apply(lambda x:x-2)
print(df)

#############################################################
#Using pandas.DataFrame.transform() to apply function column
#Using DataFrame.transform()
def add_2(x):
    return x+2
df=df.transform(add_2)
print(df)

#############################################################
#Using pandas.DataFrame.app() to Single Column
df['A']=df['A'].map(lambda A: A/2)
print(df)

#############################################################
#Using Numpy Function on single column
#Using DataFrame.apply() & [] operator
df=pd.DataFrame(data)
import numpy as np
df['A']=df['A'].apply(np.square)   #square of column A
print(df)    #if we print df again and again then it 
#will square again and again because we didn't initialize
#the dataframe

#Using NumPy.square() Method
#Using numpy.square() and [] operator
df['A']=np.square(df['A'])
df
 
############################################################
#Pandas groupby() with examples
import pandas as pd
import numpy as np
technologies=({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee':[20000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,None,1300,1400,]})
df=pd.DataFrame(technologies)
print(df)

#use groupby() to compute the sum
df2=df.groupby(['Courses']).sum()   #ex.Python=24000+22000=46000
df2

#Group by multiple columns
df3=df.groupby (['Courses','Duration']).sum()
df3

df4=df.groupby (['Courses','Duration','Fee']).sum()
df4

df5=df.groupby (['Courses','Duration','Fee','Discount']).sum()
df5   #Empty DataFrame

############################################################
#Add index to the grouoped data
#Add Row Index to the group by result
df2=df.groupby(['Courses','Duration']).sum().reset_index()
df2

#Group by on multiple columns
df3=df.groupby(['Courses','Duration']).sum()
df3

import pandas as pd
import numpy as np
technologies=({ 
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee':[20000,25000,23000,24000,26000],
    'Duration':['30days','50days','55days',None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]})
df=pd.DataFrame(technologies)
print(df)
df.columns

#Get the list of all column names from headers
column_headers=list(df.columns.values)
print("The Column Header :",column_headers)

#################################################################
 