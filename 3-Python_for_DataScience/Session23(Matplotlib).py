

#Write a python program to plot two or mmore lines and set line marker
import matplotlib.pyplot as plt
#x axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]

#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)

#set line y-limits of the current axes
plt.yline(1,8)
#set the y-limits of the current axes
plt.xlim(1,8)

#naming the x-axis
plt.xlabel('x-axis')
#naming the y-axis
plt.ylabel('y-axis')

#giving a title to my graph
plt.title('Display marker')
#function to show the plot
plt.show()

##################################################################
#Write a python program to display a bar chart of the popularity
#of programming languages
#Vertical display graph
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming language\n"+
          '''Worldwide, Oct 2017 compared to a year ago''')
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='pink')
plt.show()

#Horizontal display graph
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='green')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming language\n"+
          '''Worldwide, Oct 2017 compared to a year ago''')
plt.yticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='black')
plt.show()

##################################################################
#Write a python program to diaplay popularity of programming language
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=['red','black','green','blue','yellow','cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming language\n"+"Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='black')
plt.show()


##################################################################
#Histogram --> to understand the distribution of data
import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar,rwidth=0.8)#by default number of bins is set to 10
plt.hist(blood_sugar,rwidth=0.5,bins=4)

'''Histogram showing normal, pre-diabetic and diabetic patients
distribution

80-100: Normal
100-125: Pre-diabetic
125 onwards: Diabetic'''

plt.xlabel("Sugar Level")
plt.ylabel("Number of Patients")
plt.title("Blood Sugar Chart")
plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95, color='red')

#################################################################
#Box Plot
#Import Libraries
import matplotlib.pyplot as plt
import numpy as np

#Creating dataset
np.random.seed(10)
data=np.random.normal(100,20,200)

fig=plt.figure(figsize=(10,7))
#Creating plot
plt.boxplot(data)
#show plot
plt.show()

#################################################################
#Multiple box plots
import matplotlib.pyplot as plt
import numpy as np

#Creating dataset
np.random.seed(10)
data_1=np.random.normal(100,10,200)
data_2=np.random.normal(90,20,200)
data_3=np.random.normal(80,30,200)
data_4=np.random.normal(40,70,200)
data=[data_1,data_2,data_3,data_4]

fig=plt.figure(figsize=(10,7))

#Creating axes instance
ax=fig.add_axes([0,0,1,1])
#Creating plot
bp=ax.boxplot(data)
#show plot
plt.show()
