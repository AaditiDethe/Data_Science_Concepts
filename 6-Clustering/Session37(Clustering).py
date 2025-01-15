# Clustering:

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cluster import KMeans

#let us try to understand first how k-means works for two dimensional data, for
#that, generate random numbers in the range 0 to 1
# and with uniform probability of 1/50
X=np.random.uniform(0,1,50)
Y=np.random.uniform(0,1,50)

# Create a empty dataframe with 0 rows and 2 columns

df_xy = pd.DataFrame(columns=["X","Y"])

# assign the values of X and Y to these columns
df_xy.X=X
df_xy.Y=Y

df_xy.plot(x="X",y="Y",kind="scatter")
model1 = KMeans(n_clusters=3).fit(df_xy)

'''With data X and Y, apply Kmeans model, generate scatter plot with 
scale/font = 10
cmap = plt.cm.coolwarm:cool color cobination'''

model1.labels_
df_xy.plot(x="X",y="Y",c=model1.labels_,kind="scatter",s=10,cmap=plt.cm.coolwarm)


#########################################################################
Univ1 = pd.read_excel("C:/7-clustering/University_Clustering.xlsx")
Univ1.describe()
Univ = Univ1.drop(["State"],axis=1)
# we know that ther eis scale difference among the columns, which we 
# either by using normalization or standardization

def norm_func(i):
    x = (i-i.min())/(i.max()-i.min())
    return x
# Now apply this normalization function to Univ dataframe for all the 

df_norm = norm_func(Univ.iloc[:,1:])

'''What will be ideal cluster number, will it be 1,2 or 3'''

TWSS=[]
k = list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    
    TWSS.append(kmeans.inertia_) # total within sum of square
    
    '''KMeans inertia, also known as Sum of Squares Errors (or SSE),
       calculates the sum of the distances of all points within a cluster 
       from the centroid of the point. It is the difference between the 
       observed value and the predicted value.
       '''
       
TWSS
# As k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters");
plt.ylabel("Total_within_SS")

'''How to select value of k from elbow curve
When k changes from 2 to 3, then decrease in twss is higher than 
When k changes from 3 to 4.
When k value changes fromm 5 to 6 decrease'''

model = KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb = pd.Series(model.labels_)
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ
Univ.iloc[:,2:8].groupby(Univ.clust).mean()

Univ.to_csv("kmeans_University.csv",encoding="utf-8")
import os
os.getcwd()

