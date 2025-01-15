
#2-April-2024
#####################Python for data Science#################
'''pandas,matplotlib,numpy,seaborn
   pandas--> series, columns'''

'''A series is used to model one dimensional data,similar to list 
in python(only one column). The series object also has a few more bits of data,
including an index and a name.'''
import pandas as pd
songs2=pd.Series([145,142,38,13],name='counts')
#it is easy to inspect index of series
songs2.index
#index can be in the form of integer,string,dates
#the index can be string based, in which case pandas indicate 
#that the datatype for index is object(not string)

songs3=pd.Series([145,142,38,13],name='counts',
                 index=['Paul','John','George','Ringo'])
songs3.index
songs3
#the NaN value
'''index     x1    x2    x3
    0        25    2
    2        21    3
    3        23    4               '''

'''NaN value--> this value stands for Not a Number and usually 
ignored in arithmetic operation.(Similar to NULL in SQL)
'''
#it will give error
import pandas as pd
f1=pd.read_csv('age.csv')
f1

#inorder to fix error-->path is necessary
import pandas as pd
f1=pd.read_csv('c:/1-python/age.csv')
f1

import pandas as pd
df=pd.read_excel('c:/1-python/Bahaman.xlsx')
df
#None, NaN, nan, and null are synonyms.
#the Series object behaves similarly to a NumPy array.
import numpy as np
numpy_ser=np.array([145,142,38,13])
songs3[1]
#142
numpy_ser[1]
#they both have methods in common
songs3.mean()
numpy_ser.mean()

##############################################################
'''THE PANDAS SERIES DATA STRUCTURE PROVIDES SUPPORT FOR THE 
BASIC CRUD'''
#operation_create,read,update,and delete.
#Creation
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],    #explicitily index
name='George_Songs')
george

george=pd.Series([10,7,1,22],
name='George_Songs')
george

#Reading
'''to read or select the data from a series'''
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],    #explicitily index
name='George_Songs')
george['1968']
george['1970']

#we can iterate over data in a series as well. when iterating over series
for item in george:
    print(item)

#Updating
'''Standard index assignment opoeration works'''
george['1969']=68
george['1969']
george
