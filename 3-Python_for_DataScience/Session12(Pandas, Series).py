
#Deletion
'''The del statement appears to have problems with duplicate index'''
import pandas as pd 
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

###################################################################
#Convert Types
'''string use.astype(str)
   numeric use pd.to_numeric
   integer use.astype(int)
   # note that this will fail with NaN #
   datetime use pd.to_datetime'''
import pandas as pd
songs_66=pd.Series([3.0,None,11.0,9.0],
                   index=['George','Ringo','John','Paul'],
                   name='Counts')
songs_66.dtypes    #dtypes--> use to check datatype
#dtype('float64')
pd.to_numeric(songs_66.apply(str))
pd.to_numeric(songs_66.astype(str),errors='coerce')
#if we pass errors='coerce', we can see that it performs many formats
songs_66.dtypes
#Dealing with None
#The .fillna method will replace them with a given value
songs_66.fillna(-1)
songs_66=songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes
#NaN values can be dropped from the series using .dropna
import pandas as  pd
songs_66=pd.Series([3,None,11,9],
                   index=['George','Ringo','John','Paul'],
                   name='Counts')
songs_66=songs_66.dropna()
songs_66

##################################################################
#Append, combining, and joining two series
import pandas as pd
songs_66=pd.Series([3.0,None,11.0,9.0],
                   index=['George','Ringo','John','Paul'],
                   name='Counts')
songs_69=pd.Series([7,16,21,39],
                   index=['Ram','Sham','Ghansham','Krishna'],
                   name='Counts')
#to concatinate two series together, simply use the .append()
songs=pd.concat([songs_66,songs_69])
songs

##################################################################
#plotting series
import matplotlib.pyplot as plt
fig=plt.figure()
songs_69.plot()
plt.legend()

import matplotlib.pyplot as plt
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

import numpy as np
data = pd.Series(np.random.randn(500),name='500_random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()