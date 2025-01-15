
import pandas as pd
import matplotlib.pylab as plt
# Now import file from data set and create a dataframe
Univ1=pd.read_excel("C:/7-clustering/University_Clustering.xlsx")
a=Univ1.describe()
a
# We have one column "State" which really not useful we will drop that column
Univ=Univ1.drop(["State"],axis=1)
Univ
# We know that there is scale difference among the columns, which we have to remove
# either by using normalization or standardization
# Whenever there is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
# Now apply this normalizationfunction to Univ dataframe
# For all the rows and column from 1 until ens
# since 0th column has University name hence skipped
df_norm=norm_func(Univ.iloc[:,1:])
df_norm
# You can check the df_norm dataframe which is scaled between values from 0 to 1
# you can apply describe function to new data frame
b=df_norm.describe()
b
# before applying clustering , you need to plot dendogram
# now create dendogram need to calculate distance/ measure distance, we have
# to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
# Linkage function gives us hierarchical or aglomerative clustering
# ref the help for linkage
z=linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8));
plt.title("Hierarchical Clustering dendogram");
plt.xlabel("Index");
plt.ylabel("Distance")
# ref help of dendogram
# sch.dendogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
# dendrogram
# applying agglomerative clustering choosing 5 as clusters from dendrogram
# whatever has been displayed in dendogram is not clustering
# it is just showing number of possible clusters
from sklearn.cluster import AgglomerativeClustering 
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',
                                   metric='euclidean').fit(df_norm)
# metric or affinity --> will work
# affinity has been depricated, use metric
# apply labels to the clusters 
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
# Assign this series to Univ DataFrame as column and name the column 
Univ['clust']=cluster_labels
# we want to relocate the column 7 to 0 th position
Univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]
# now check the Univ1 dataframe
Univ1.iloc[:,2:].groupby(Univ1.clust).mean()
# from the output cluster 2 has got highest TOP10
Univ1



