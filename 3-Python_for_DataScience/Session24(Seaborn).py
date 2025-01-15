
#Box-plot: to understand the data distribution
'''Seaborn'''
import seaborn as sns
import pandas as pd
sales=pd.read_excel("C:/1-python/sales.xlsx")
sales.head()
sales.columns
cars=pd.read_csv("c:/1-python/Cars.csv")
cars.columns
sns.relplot(x='HP',y='MPG',data=cars)
sns.relplot(x='HP',y='MPG',data=cars,kind='line')
sns.catplot(x='HP',y='MPG',data=cars,kind='box')
sns.distplot(cars.HP)

########################################################3
import pandas as pd
import numpy as np
import seaborn as sns
cars=pd.read_csv("c:/1-python/Cars.csv")
cars.describe()

#Graphical representation
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.distplot(cars.HP)
#data is right skewed
plt.boxplot(cars.HP)
#There are several outline
plt.boxplot(cars.MPG)
sns.distplot(cars.MPG)

sns.distplot(cars.VOL)
plt.boxplot(cars.VOL)

sns.distplot(cars.SP)
plt.boxplot(cars.SP)
#There are several outliers

sns.distplot(cars.WT)
plt.boxplot(cars.WT)
#There are several outliers
#Now let us plot joint plot
import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars['MPG'])

#Count plot
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])
#count plot shows how many times the each value occured 92 HP value occurred
#7 times