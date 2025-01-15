
#assignment operation
#This will create a new variable with the same reference
list_a=[1,2,3,4,2]
list_b=list_a
list_a[0]=-10
print(list_a) 
print(list_b)    


##Shallow copyyy
import copy
list_a=[1,2,3,4,2]#one level
list_b=copy.copy(list_a)
#not affect the other list
list_b[0]=-10
print(list_a) 
print(list_b)

#with nested object modifying level two
list_a=[[1,2,3,4,2],[2,3,4,5]]#two level
list_b=copy.copy(list_a)
list_a[0][0]=-10
print(list_a) 
print(list_b)

#with nested object modifying level two
list_a=[[1,2,3,4,2],[2,3,4,5]]#two level
list_b=copy.copy(list_a)
list_b[0][0]=-10
print(list_a) 
print(list_b)
    
##Deep copy
list_a=[[1,2,3,4,2],[2,3,4,5]]#two level
list_b=copy.deepcopy(list_a)
list_a[0][0]=-10
print(list_a) 
print(list_b)   
# only list_a have changes not list_b

list_a=[[1,2,3,4,2],[2,3,4,5]]#two level
list_b=copy.deepcopy(list_a)
list_b[0][0]=-10
print(list_a) 
print(list_b)   
#################################################################
#Reading data in various formats
#read csv file
import pandas as pd
f1=pd.read_csv('C:/1-Python/buzzers.csv')
f1
#check for the working directory
import os
with open('C:/1-Python/buzzers.csv') as raw_data:
    print(raw_data.read())   #read() --> read content of the file

#reading csv file/data as a list
import csv
with open('C:/1-Python/buzzers.csv') as raw_data:
    print(raw_data.read())
    
import pandas as pd
f1=pd.read_csv('buzzers.csv')   #path is compulsory

#reading csv file/data as a list
import csv
with open('C:/1-Python/buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)

#Reading CSV data as dictionaries
'''data in the form of dictionary'''
import csv
with open('C:/1-Python/buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)

import csv
with open('C:/1-Python/buzzers.csv') as data:
    #ignore=data.readline()
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights

#################################################################
#Pre-requisite to decorators
def plus_one(number):
    number1=number+1
    return number1
plus_one(5)

#Defining function inside other functions
'''Not recursive function'''
def plus_one(number):
    
    def add_one(number):
        number1=number+1
        return number1
    
    result=add_one(number)    
    return result
plus_one(4)

def name(nam):
    def name(nam):
        return nam
    #it creates some object so it should be store in another variable
    result=name(nam)
    return result
name("Aaditi")

#Passing function as arguments to other functions
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result
function_call(plus_one)

#Function returning other function
def hello_function():
    def say_hi():
        return "hi"
    return say_hi
#hello_function() --> return only object
hello=hello_function()
hello()

################################################################
#Need for decorators (imp question)
'''how much time required to perform the given task'''
import time
def calc_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution square is {total_time}")
    return result

def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution cube is {total_time}")
    return result

array=range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
'''In above-->May get different results'''

