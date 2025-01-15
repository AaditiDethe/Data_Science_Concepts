
# Python - String , List

#Python programming to print odd numbers in a range
start, end=4,19
#iterating each number in list
for num in range(start,end+1):
    #condition checking
    if num % 2!=0:
        print(num, end=" ")

########################################################
#Python program for even numbers
start,end=4,19
for num in range(start,end+1):
    if num%2==0:
        print(num,end=" ")
        
########################################################
x,y,z=1,2,3
print(x)
print(y)
print(z)
x,y,z=5  #not allowed (cannot unpack non-iterable int object)
x=y=z=5
print(x)
print(y)
print(z)

########################################################
#Global Variables
x="awesome"
def my_func():
    print("Python is",x)
my_func()

########################################################
#Global and Local variables
x="awesome"
def my_func():
    x="fantastic"
    print("Python is "+x)  #priority is given to local variable
my_func()
print("Python is "+x)

########################################################
#Getting datatypes
#integer
x=5
print(type(5))

#range
x=range(6)
print(type(x))

########################################################
#dictionary
x={'name':'ram','age':34}
print(type(x))
#OUTPUT: <class 'dict'>
########################################################
#This will give an error beacause string and int can not be concatinated
str1="Hello"
str2=2
str3=str1+str2
print(str3)
# TypeError: can only concatenate str (not "int") to str

#to fix this error
str1="Hello"
str2=" 2"
str3=str1+str2
print(str3)
########################################################
#String
#Multiplying a string
x="""This is python.It is very powerful."""
print(x)
print(2*x)

x="""This is python.
It is very powerful."""
print(x)
print(2*x)

#String sciling
x="Python is very powerful."
a=len(x)
print(a)
print(x[2:8])
print(x[:8])   #sciling from start
print(x[4:])
print(x[-5:-2])
print(x[-2:-5])   #no output

#Modify string
#strip
x="This is python. It is powerful."
print(x.upper())  #all alphabets in uppercase of string
y=x.upper()
print(y.lower())

x=" This is Python."
print(x.strip())  #removes space

x=" This is Python.   "
print(x.strip())  #removes space from both the ends

#replace
x="Hello World"
print(x.replace("Hello","Gello"))  #replaces Hello by Gello

#split
x="Hello World !"
print(x.split(" "))

#Reversing of string
x="Hello World"
string1=x[::2]
print(string1)

x="Hello World"
string1=x[::-2]  #reverse order but displacement by 2
print(string1)

x="Hello World"
string1=x[::-1]  #reverse order string
print(string1)

#Find method
'''finds location of particular word.
used in machine learning'''
x="This is Python and it is powerful."
print(x.find("and"))
print(x.find("a"))

#String Concateness
x="hello"
y="world"
print(x+y)       #adds no space
print(x+" "+y)   #adds space(white space)

#it will give error as we cannot concatinate string with integer
x=39
y="My name is Anthony"
print(x+y)
'''as above code gives error use 'f' operator to 
   concatinate string with integer'''
age=39
print(f"My name is Anthony and my age is {age}")

#######################################################
quantity=3
item_no=54
price=67   #provided with and without whitespace in print statement
print(f"I want {quantity} pieces and item number {item_no} with price {price}")
print(f"I want{quantity} pieces and item number {item_no}with price {price}")

#######################################################

#another method to cancate int with string
quantity=33
item_no=54
price=673 
my_order="I want {} pieces and item number is {}, its price is{}"
print(my_order.format(quantity,item_no,price))

#######################################################
quantity=33
item_no=54
price=673 
my_order="I want {0} pieces and item number is {1}, its price is {2}"  #it will generate id starting from 0
#id starts from 0
print(my_order.format(quantity,item_no,price))

#######################################################
#embide quoted statements
'''The escape characters allows you to use double quotes when
   you want to use quotes within quotes'''
text="This is fun fair and it has got big \"round rigo\""
#text="This is fun fair and it has got big "round rigo""  ---> will give error
print(text)

#######################################################
#Python boolean
#Comparison Operator
print(10>9)
print(10<9)
print(10==10)

#######################################################
'''Rules for mathematical operations
   PEMDAS
   P:paranthesis
   E:Exponential
   M:Multiplication
   D:Division
   A:Addition
   S:Subtraction'''
#Operator Precedence
print(3*3+3/3-3)  #output will be 7.0 i.e float datatype

print(3.0+3) #float
print(3+5)  #integer
#######################################################
#Identity operator
a=2
b=3
print(a is b)
print(a is not b)

#######################################################
#Python list
'''1.List items are indexed starting from 0 (first index) to n(positive indexing)
    and from -1(negative indexing)'''
list=["cherry","banana","apple"]
print(list)
print(list[0])
print(list[-1])
print(list[2])

#append() method
'''Adds a new element to the list'''
lst=["cherry","banana","apple"]
print(lst)
lst.append("mango")
print(lst)
print(lst.append("mango"))  #OUTPUT: None

#clear() method
'''clear() removes all the elements from the list --> empty list []'''
lst=["cherry","banana","apple"]
print(lst)
lst.clear()
print(lst)

#copy() method
lst=["cherry","banana","apple"]
print("List is: ",lst)
lst2=lst.copy()
print("Lst2 is: ",lst2)

'''features:
    1.repeated data types are also allowed
    2.Can contain different data types
    3.Mutable-change the data quantities.
    '''
#count() 
'''Returns number of times the value "cherry" is presenr'''
lst=["cherry","banana","apple","cherry","Cherry"]
lst.count("cherry")

#extend() method
'''Adds the elements of one list to another list at the end'''
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)
#OUTPUT : [1, 2, 3, 4, 5, 6]
lst=[1,2,3]
lst1=[4,5,6]
lst.append(lst1)
print(lst)

#OUTPUT: [1, 2, 3, [4, 5, 6]]
l1=['A','B']
l1.append('C')
print(l1)


#insert() method
'''insert the value at a specified position.
   This is also calles mutation and list is mutable'''
lst=["cherry","banana","apple"]
lst.insert(1,"Mango")
print(lst)


#pop()
'''give index of the entity to be removed'''
lst=["cherry","banana","apple"]
lst.pop(2)
print(lst)

#remove()
'''using name of entity to be removed'''
lst=["cherry","banana","apple"]
lst.remove("cherry")
print(lst)

lst=["cherry","banana","apple","cherry"]
lst.remove("cherry")
print(lst)
lst.remove("cherry")
print(lst)
'''here which ever is the first cherry(cherry located
   at the first any index) will be removed
   if there are more than 1 cherry. To remove 2nd cherry
   again use the remove() method'''
   
#reverse() method
lst=["cherry","banana","apple"]
lst.reverse()
print(lst)

#sort() method
'''sort the list in alphabetical order'''
lst=["cherry","orange","banana","apple"]
lst.sort()
print(lst)

#######################################################
#Tuples
tup=("cherry","cherry","banana")
print(tup)

#entity of tuple using index number
tup=("cherry","cherry","banana")
print(tup[2])
print(tup[0])
print(tup[-2])

'''features of tuple:
    1.immutable---> to be mutable change tuple into list
    2.It allows mixed data types.'''
#once a tuple is created
x=("apple","banana","cherry")
#x[1]="kiwi"
#first convert into list
y=list(x)
print(y)
y[1]="kiwi"
#convert list into tuple
x=tuple(y)
print(x)

#Mixed data types
x=("apple",2,"cherry")
print(x)

x=("apple","cherry","banana")
print(x[2])     #displays the 3rd element of the tuple

#To join two or more tuples you can use the +operator
tuple1=("a","b","c")
tuple2=(1,2,3)
tup=tuple1+tuple2
print(tup)

#######################################################
#Dictionary
dict1={"Brand":"Maruti","model":"2345","year":2024}
print(dict1)
print(len(dict1))
print(type(dict1))

dict={"Brand":["Maruti","Mahendra","Toyato"],"Model":["a","b","c"],"Year":[2023,2034,2056]}
print(dict)

#get()
'''displays key and value'''
dict1={"Brand":"Maruti","model":"2345","year":2024}
dict1.get("model")
dict1.keys()
dict1.values()

