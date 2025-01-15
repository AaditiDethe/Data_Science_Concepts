
#Stack Overflow-->useful for data scientist (website)
#index array out of bounds
from numpy import array#define array
data=array([11,22,33,44,55])
#index data
print(data[4]) #OUTPUT --> 55
print(data[5])
'''OUTPUT --> 
IndexError: index 5 is out of bounds for axis 0 with size 5'''

#index row of 2 dimensional array
from numpy import array
#define array
data =array([
    [11,22],
    [33,44],
    [55,66]])
#index data
print(data[0,]) # 0th row and all columns
#OUTPUT --> [11 22]

###############################################
#Slicing
#slice a 1 dimensional array
from numpy import array
#define array
data=array([11,22,33,44,55])
print(data[1:4])
#OUTPUT --> [22 33 44]

#negative slicing of 1-D array
from numpy import array
#define array
data=array([11,22,33,44,55])
print(data[-2:])
#OUTPUT --> [44 55]

###############################################
#Split input and output data
from numpy import array
#define array
data=array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#separate data
x,y=data[:,:-1],data[:,-1]
x
y
#data[:,:-1]- all rows and columns 0 and 1
#all rows and last column

###############################################
'''BroadCast -->  only number then scalar
[1,2,3] - vector
[[12.3]
 [2 4 6]]   matrix
and then tensor
'''
#broadcast scalar to 1-D array
from numpy import array
#define array
a=array([1,2,3])
print(a)
#define scalar
b=2
print(b)
#broadcast
c=a+b
print(c)


from numpy import array
#define array
a=array([1,2,3])
print(a)
#define scalar
b=2
print(b)
#broadcast
c=a*b
print(c)
###############################################
#Vector L1 norm
'''sum of absolute vector values
||v||1 = |a1| + |a2| +|a3|
The L1 norm is calculated as the sum of the absolute vector values,
where the absolute value of scalar uses the notation |a1|.
In effect, the norm is a calculated of the Manhattan distance
from the origin of the vector space.
||v||1 = |a1| + |a2| +|a3|'''

from numpy import array
from numpy.linalg import norm
#define array
a=array([1,2,3])
print(a)
#calculate norm
l1=norm(a,1)
print(l1)

'''The notation for the L2 norm of a vector x is ||x|| power of
2.
To calculate the L2 norm of a vector, take teh square root of 
the sum of the squared vector values.
Another name for L2 norm of a vector is Euclidean distance.
This is often used for calculating the error in machine learning 
models.'''
#Vector L2 norm
from numpy import array
from numpy.linalg import norm
#define array
a=array([1,2,3])
print(a)
#calculate norm
l2=norm(a) #1+4+9=14 under root of 14 is 3.74
print(l2)

############################################
#Triangular matrix
from numpy import array
from numpy import tril
from numpy import triu
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)

#lower triangular matrix
lower=tril(M)
print(lower)
'''OUTPUT --> 
[[1 0 0]
 [1 2 0]
 [1 2 3]]'''

#upper triangular matrix
upper=triu(M)
print(upper)
'''OUTPUT --> 
[[1 0 0]
 [1 2 0]
 [1 2 3]]'''

############################################
#Diagonal Matrix
from numpy import array
from numpy import diag
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)
#extract diagonal vector
d=diag(M)
print(d)
'''OUTPUT --> [1 2 3]'''

#create diagonal matrix from vector
D=diag(d)
print(D)
'''OUTPUT -->
[[1 0 0]
 [0 2 0]
 [0 0 3]]'''

############################################
#Identity Matrix
from numpy import identity
I=identity(3)
print(I)
'''OUTPUT --> 
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]'''

############################################
#Orthogonal Matrix
'''The matrix is said to be orthogonal matrix if the product 
of a matrix and its transpose gives an identity value.'''

from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
Q=array([
    [1,0],
    [0,-1]])
print(Q)

#inverse equivalence
V=inv(Q)
print(Q.T)
print(V)

#identity equivalence
I = Q.dot(Q.T)
print(I)

#Transpose
from numpy import array
#define matrix
A=array([
    [1,2],
    [3,4],
    [5,6]])
print(A)
#calculate transpose
C=A.T
print(C)

######################################################
#inverse matrix
from numpy import array
from numpy.linalg import inv
#define matrix
A=array([
    [1.0,2.0],
    [3.0,4.0]])
print(A)
#inverse matrix
B=inv(A)
print(B)
#multipl A and B
I=A.dot(B) #identity matrix
print(I)

#######################################################
#sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
#create dense matrix
A=array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)
#convert to sparse matrix (CSR method)
S=csr_matrix(A)
print(S)
#reconstruct dense matrix
B=S.todense()
print(B)
