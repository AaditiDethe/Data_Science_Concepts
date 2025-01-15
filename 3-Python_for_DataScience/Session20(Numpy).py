# Numpy
import numpy as np
multi_array=np.array([[10,20,10,20],
                      [40,50,70,90],
                      [60,10,70,80],
                      [40,90,80,30]])
multi_array
x=multi_array[:3,::2]
print(x)

#Integer array indexing
arr=np.arange(35).reshape(5,7)
print(arr)

#Boolean array indexing
'''Define Boolean array'''
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array([False,True,True]) #0th row will be vomited
rows
wanted_rows=arr[rows,:]
print(wanted_rows)
#[[ 4  5  6  7]
# [ 8  9 10 11]]

##################################################################
#numpy.asarray(): using numpy.asarray() --> same as np.array
#Use asarray() 
list=[20,40,60,80]
array=np.asarray(list)
print("Array:",array)
print(type(array))
#Output--> Array: [20 40 60 80]
#          <class 'numpy.ndarray'>

#Numpy Array Properties
'''ndarray.shape
   ndarray.ndin
   ndarray.itemsize
   ndarray.size
   ndarray.dtype'''
#ndarray.shape--> to get the shape of Python NumPy array use numpy

#Shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
#array([[1, 2, 3],
#      [4, 5, 6]])
#(2, 3) --> row,column

#Resize the array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)
#Output --> [[10 20]
#            [30 40]
#            [50 60]]

#reshape usage
array=np.array([[10,20,30],[40,50,60]])

#################################################################
#Arithmetic Operations
#Apply arithmetic operations on numpy arrays
arr1=np.arange(16).reshape(4,4)
arr1
arr2=np.array([1,3,2,4])
arr2

#add()
add_arr=np.add(arr1,arr2)
print(f"Adding two arrays:\n{add_arr}")

'''OUTPUT --> 
Adding two arrays:
[[ 1  4  4  7]
 [ 5  8  8 11]
 [ 9 12 12 15]
 [13 16 16 19]]'''

#subtract()
sub_arr=np.subtract(arr1,arr2)
print(f"Subtracting two arrays:\n{sub_arr}")

'''OUTPUT --> 
Subtracting two arrays:
[[-1 -2  0 -1]
 [ 3  2  4  3]
 [ 7  6  8  7]
 [11 10 12 11]]'''

#multiply()
mul_arr=np.multiply(arr1,arr2)
print(f"Multiplying two arrays:\n{mul_arr}")

'''OUTPUT --> 
Multiplying two arrays:
[[ 0  3  4 12]
 [ 4 15 12 28]
 [ 8 27 20 44]
 [12 39 28 60]]'''
              
#division()
div_arr=np.divide(arr1,arr2)
print(f"Dividing two arrays:\n{div_arr}")

'''OUTPUT --> 
Dividing two arrays:
[[ 0.          0.33333333  1.          0.75      ]
 [ 4.          1.66666667  3.          1.75      ]
 [ 8.          3.          5.          2.75      ]
 [12.          4.33333333  7.          3.75      ]]'''

#################################################################
#numpy.reciprocal()
#To perform Reciprocal Operation
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"After applying reciprocal function to array:\n{rep_arr1}")

'''OUTPUT --> 
After applying reciprocal function to array:
[0.02       0.09708738 0.2        1.         0.005     ]'''

#################################################################
#numpy.power()
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"After applying power function to array:\n{pow_arr1}")

'''OUTPUT --> 
After applying power function to array:
[  27 1000  125]'''

arr1=np.array([3,10,5])
arr2=np.array([3,2,1])
print("My first array:\n",arr1)
print("My second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"After applying power function to array:\n{pow_arr2}")

'''OUTPUT --> 
After applying power function to array:
[ 27 100   5]'''

#################################################################
#numpy.mod()
#To perform mod function on NumPy array
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr2
arr1.dtype
arr2.dtype

#mod()
mod_arr=np.mod(arr1,arr2)
print(f"After applying mod function to array:\n{mod_arr}")

'''OUTPUT -->
After applying mod function to array:
[1 0 1]'''

#################################################################
#Create an empty array
from numpy import empty
a = empty([3,3])
print(a)


#Create zero array
from numpy import zeros
a = zeros([3,5])
print(a)

'''OUTPUT --> 
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]'''

#Create one array
from numpy import ones
a = ones([5])
print(a)

'''OUTPUT --> 
[1. 1. 1. 1. 1.]'''

#Create array with vstack
from numpy import array
from numpy import vstack
#create first array
a1 = array([1,2,3])
print(a1)
#create second array
a2 = array([4,5,6])
print(a2)
#vertical stack
a3 = vstack((a1,a2))
print(a3)
print(a3.shape)

#################################################################
#Create array with hstack
from numpy import array
from numpy import hstack
#create first array  
a1 = array([1,2,3])
print(a1)
#create second array
a2 = array([4,5,6])
print(a2)
#horizontal stack
a3 = hstack((a1,a2))
print(a3)
print(a3.shape)
 
