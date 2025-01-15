
# K-Means clustering (Numerical data)
from sklearn.cluster import KMeans #Import KMeans algorithm from sklearn library, which will be used for clustering
import pandas as pd   # Pandas for handling data structure, such as DataFrames
from sklearn.preprocessing import MinMaxScaler   # For feature scaling
from matplotlib import pyplot as plt  # For Data Visualization

# Now load the data
df = pd.read_csv("C:/7-clustering/income.csv")  
# pd.read_csv(): Reads the dataset income.csv from the specified path and stores it in the df DataFrame

df.head()
#df.head() # Displays the first 5 rows of the dataframe to understand the structure of the dataset

df.columns
# Shows the names of columns(features)

# Scatter Plot (Age vs Income)
plt.scatter(df.Age,df['Income($)'])  
plt.xlabel('Age')
plt.ylabel('Income($)')

# Initializes the KMeans clustering algorithm with 3 clusters.
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])
# km.fit_predict(): Applies the KMeans algorithm to the Age and Income columns.
#It fits the model and predicts the cluster labels for each data point

# Stores the predicted cluster labels for each data point.
y_predicted

# Assign Cluster Labels to Data 
df['cluster']=y_predicted   # Adds a new column called cluster to teh DataFrame,
# where each datapoint is assigned to aa cluster (0,1,2)

df.head()

km.cluster_centers_


df1 = df[df.cluster==0] 
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],
            color='purple',marker='*',label="centroid")
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.legend()
'''Here we have created 3 clusters [0], [1] and [2] and have assign color
to it. There will be purple color centroid'''

#Preprocessing using min max 
scaler=MinMaxScaler()

scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])
df.head()


plt.scatter(df.Age,df['Income($)'])

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])
y_predicted

df['cluster']=y_predicted
df.head()

km.cluster_centers_


df1 = df[df.cluster==0] 
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],
            color='pink',marker='*',label="centroid")
#plt.xlabel('Age')
#plt.ylabel('Income($)')
plt.legend()


######################################################################
