# Matplotlib:
 
'''df.describe() --> 5 number summary mean,min,max,25% value,50%
                      value,75% value '''

#Write a Python program to draw a line with suitable label
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value * 3 for value in X]
print("Values of X: ")
print(*range(1,50))    #not included 50
'''This is equivalent to-
   i in range(1,50):
       print(i, end=' ')'''
print("Values of Y (thrice of X): ")
print(Y)
#Plot lines and/or markers to the Axes.
plt.plot(X,Y)
#Set the x axis label of the current axis
plt.xlabel('x - axis')
#Set the y axis label of the current axis
plt.ylabel('y - axis')
#Set a title
plt.title('Draw a line.')
#Display the figure
plt.show()


#label in the x-axis ,y-axis and a title.
import matplotlib.pyplot as plt
# x axis values
x=[1,2,3]
# y axis values
y=[2,4,1]
#Plot lines and/or markers to the Axes
plt.plot(x,y)
# Set the x-axis label of the current axis
plt.xlabel('x - axis')
#Set the y axis label of the current axis
plt.ylabel('y - axis')
#Set a title
plt.title('Sample Graph.')
#Display the figure
plt.show()

#Write a Python program to plot two or more lines
#on some plots with suitable legends of each line.
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#plotting the line 1 points
plt.plot(x1,y1,label = "Line 1")
#plotting the line 2 points
plt.plot(x2,y2,label="Line 2")
#Set the x axis label
plt.xlabel('x - axis')
#Set the y axis label of the current axis
plt.ylabel('y - axis')
#Set the title of the current axis
plt.title('Two or more lines on same plot with suitable legends of each line')
#show a legend on the plot
plt.legend()
#Display a figure
plt.show()


#With color lines
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#Set the x axis label of the current axis
plt.xlabel('x - axis')
#Set the y axis label of the current axis
plt.ylabel('y - axis')
#Set the title of the current axis
plt.title('''Two or more lines with different widths 
          and colours on same plot with suitable legends 
          of each line''')
#Display the figure
plt.plot(x1,y1,color='blue',linewidth =3 ,label = "Line 1")
#plotting the line 2 points
plt.plot(x2,y2,color='red',linewidth =5, label="Line 2")
#show a legend on the plot
plt.legend()
#Display a figure
plt.show()

#lines --> dash and dotted
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#Set the x axis label of the current axis
plt.xlabel('x - axis')
#Set the y axis label of the current axis
plt.ylabel('y - axis')
#Set the title of the current axis
plt.title('''Two or more lines with different styled''')
#Display the figure
plt.plot(x1,y1,color='blue',linewidth =3 ,label = "Line1-dotted",linestyle='dotted')
#plotting the line 2 points
plt.plot(x2,y2,color='red',linewidth =5, label="Line2-dashed",linestyle='dashed')
#show a legend on the plot
plt.legeng()
#Display a figure
plt.show()

