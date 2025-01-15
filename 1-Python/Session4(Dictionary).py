# Dictionary:

car={"brand":"ford","model":"mustang","year":1964}
x=car.keys()
print(x)
car["color"]="white"
x=car.keys()
print(x)
car

car={"brand":"ford","model":"mustang","year":1964}
x=car.keys()
print(x)
car["color"]="white"
car
x=car.keys()
print(x)

#########################################################
#Removing the dictionary element
#pop method in dictionary required keys
car={"brand":"ford","model":"mustang","year":1964}
car.pop("model")
print(car)

#Accessing keys in the dictionary
car={"brand":"ford","model":"mustang","year":1964}
for x in car:
    print(x)

#Accessing values in the dictionary
car={"brand":"ford","model":"mustang","year":1964}
for x in car:
    print(car[x])

#Accessing both values and keys in the dictionary
car={"brand":"ford","model":"mustang","year":1964}
for key,value in car.items():
    print("%s = %s"%(key,value))

#Coping Dictionary
car={"brand":"ford","model":"mustang","year":1964}
car2=car.copy()
car2
print(car2)    #print(car2)  and car2 --> same

#Another way to make a copy
thisdict={"brand":"ford","model":"mustang","year":1964}
dict1=dict(thisdict)
dict1

#A dictionary can contain dictionaries,this is called nested dictionary
our_family={"child":{"name":"ram","DOB":"01-01-2008"},"child2":{"name":"shyam","DOB":"01-01-3004"}}
our_family

#########################################################
#Dictionary Method
#clear()
'''Remove all elements from car(dictionary)'''
car={"brand":"ford","model":"mustang","year":1964}
car.clear()
car

#fromkey()
#create a dictionary with 3 keys all with respective keys
x={'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict

#get()
'''to get the value of the dictionary'''
car={"brand":"ford","model":"mustang","year":1964}
car.get("model")

#items()
'''return the dictionary's key-value'''
car={"brand":"ford","model":"mustang","year":1964}
car.items()

#values()
'''display all the values of dictionary'''
car={"brand":"ford","model":"mustang","year":1964}
car.values()

#update
'''insert an item in the dictionary'''
car={"brand":"ford","model":"mustang","year":1964}
car.update({"color":"orange"})
car
  
#########################################################
#for loop
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)

########################################################
#break statement
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if(i=="banana"):
        break
'''here if specified value is found then it will break
   it. It will print apple banana only '''

fruits=["apple","banana","orange"]
for i in fruits:
    if(i=="banana"):
        break
    print(i)
'''here it will not print banana'''

########################################################  
#Continue
'''used to continue the loop''' 
fruits=["apple","banana","orange"]
for i in fruits:
    if(i=="banana"):
        continue
    print(i)
'''initially it will take x=0 which is apple'''

########################################################
#range()
for x in range(2,6):
    print(x)

for x in range(2,30,3):
    print(x)
    
########################################################
#nested loop
'''Nested loop--> loop in loop
   "inner loop" --> will be executed one time'''
color=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in color:
    for y in fruits:
        print(x,y)

########################################################
#Function
#function without argument
def my_function():
    print("Hello from a function")
my_function()

#function with arguments
def my_function(name):
    print("My name is:",name)
my_function("Aaditi")

def my_function(name):
    print("My name is:"+name)
my_function("Aaditi")

'''Function with more than two arguments'''
def my_function(name1,name2):
    print(name1+" "+name2)
my_function("World","Hello")

#Arbitary arguments
'''symbol--> *args
If you don't know how many arguments that will be passed
 in the function we use arbitary arguments'''
def my_func(*kids):
    print(kids[0]+" "+kids[2])
my_func("Hello","World","India")

########################################################
#kwargs
#keyword argument
def my_function(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" %(key,value))
my_function(first='papalala',mid='mohanlal',last='goyal')

#default parameter
'''1.it will call function without argument
   2.it uses the default argument'''
def my_func(country="Norway"):
    print("I am from "+country)
my_func("Sweden")
my_func("India")
my_func()
my_func("Brazil")

#Passing a list as an argument
fruits=["orange","banana","guava"]
def my_func(fruits):
    for x in fruits:
        print(x)
my_func(fruits)

#Return values
'''to let the function return a value,use the return 
   statement'''
def my_fun(x):
    return x*5
my_fun(4)

#pass function
def my_func():
    pass
'''having an empty function definition
   like this, would raise an error without the pass 
   statements'''
   
########################################################
#Finding out the factorial of the number
'''function inside function is called recursive function'''
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(6)
factorial(3)
'''5*factorial(4)'''


def factorial(x):
    if x==1:
        return 1
    elif x==0:
        return 1
    else:
        return(x*factorial(x-1))
factorial(0)
########################################################
#A lamda function-->anonymous function
'''It can take any number of arguments but can only 
   have one expression'''
#simple function
def add(a):
    sum=a+10
    return sum
add(20)

#lambda function
add=lambda a:a+10
print(add(20))
'''here add is function -->add()'''

#Lambda function can take any number of arguments
add=lambda a,b:a+b
print(add(12,34))

#Finding odd numbers from list
'''here odd_lst is a function'''
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2 != 0),lst))
print(odd_lst)

'''The filter() method accepts two arguments in python
   a function and an interable such as list.
   Whenever we use iterator we use filter.'''
   
#Finding out the even numbers from list:
lst=[34,12,64,55,75,13,63]
even_lst=list(filter(lambda x:(x%2 == 0),lst))
print(even_lst)

#Displaying square of numbers:
lst=[1,2,3,4,5,6,7,8,9,10]
sqr_lst=list(filter(lambda x:(x**2),lst))
print(sqr_lst)
