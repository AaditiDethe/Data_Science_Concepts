
####list comprehension####
list=[]
for num in range(0,20):
    list.append(num)
print(list)

list=[]
for num in range(0,20):
    print(num)

##by list comprehension
list=[num for num in range(0,20)]
print(list)


names=["dada","mama","kaka"]
list=[name.capitalize() for name in names]
print(list)


#comprehension with if statement
def is_even(num):
    return num%2==0
list=[num for num in range(21) if is_even(num)]
print(list)

#comphrension with nested for loop 
list=[f"{x}{y}"for x in range(3) for y in range(3)]
print(list)

##dict comprehension
dict={x:x*x for x in range(3)}
print(dict)

###Generator
'''It is another way of creating iterators in a simple way
where it uses the key word "yield".Instead of returning
it in a defined function.
Generators are implemented using a function.
Generator is object type.'''

#generator for all values
#gen is handle or reference
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

#generator for single values
gen=(x for x in range(3))
next(gen)
next(gen)

##functions which return multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
    
#now instead of using for loop we can write create generators
gen=range_even(6)
next(gen)
next(gen)
    
###chaining generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*"*"
        
password=["not good","give m-pass"]    
for password in hide(lengths(password)):
    print(password)
    
        
'''"ele*" appears to be a placeholder for an element
from an iterable.The asterisk(*) is likely just a character
used to represent a placeholder or a wildcard.
for instance if u r iteratngover a lst of elemts,"ele*"
could symbolize any representation that does not  correspond to any specific syntax
in python or itertolls'''


##take password from user and hide it
adj=input("Enter an adj:")
noun=input("Enter a noun:")
number=input("Enter a number:")
sc=input("Enter a special character:")
password=adj+noun+str(number) +sc
print("Your password is: %s"%password) 
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele* "*"
password=adj+noun+str(number)+sc    
for password in hide(lengths(password)):
    print(password,end="") 

################################################################
#Enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')    #indexing from 1

lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index} {lst[index]}')      #indexing from 0
    
#Same code can be implemented using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=0):   #indexing from 0
    print(f"{index} {item}")

lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):   #indexing from 1
    print(f"{index} {item}")

################################################################
#Use of zip function:
'''Accessing two list at a time'''
name=["dada","mama","kaka"]
info=[324,435,678,345]
for nm,inf in zip(name,info):
    print(nm,inf)
    
#Use of zip function with mis match list
name=["dada","mama","kaka","baba"]
info=[1234,3245,5456]
for nm,inf in zip(name,info):
    print(nm,inf)
'''It will not display excess mismatch item in name i.e baba'''

#zip longest
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[2345,4633,5667]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
    
#use of fill value instead of None
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[2345,4633,5667]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

################################################################
#use of all()
'''If all the values are true then it will produce output'''
lst=[2,3,-6,8,9]    #value should be non zero, +ve or -ve
if all(lst):
    print("All values are true!")
else:
    print("There are null values")
    
lst=[2,3,0,8,9]   
if all(lst):
    print("All values are true!")
else:
    print("There are null values")

################################################################
#any()
'''if any one non zero value'''
lst=[0,0,0,-8,0]
if any(lst):
    print("It has some non zero value.")
else:
    print("All values are zero in the list.")

lst=[0,0,0,-0]
if any(lst):
    print("It has some non zero value.")
else:
    print("All values are zero in the list.")

lst=[0,0,0,0]
if any(lst):
    print("It has some non zero value.")
else:
    print("All values are zero in the list.")

################################################################
#count()
'''used in image processing'''
from itertools import count
counter=count()
print(next(counter))  #count starts from 0
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
    
#Now lets start from 1
from itertools import count
counter=count(start=1)
print(next(counter))  #count starts from 1
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

################################################################
#cycle()
'''Suppose you have repeated task to be done, then use cycle()'''
import itertools
instructions=("Eat","Code","Sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
    
################################################################
'''Data Synchrounization'''
#repeat()
'''Itertool-->repeat'''
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)

################################################################
'''permutations--> arrangenment in sequence
   combination--> combining'''
#combinations()
from itertools import combinations
players=["John","Jani","Janardhan"]
for i in combinations(players,2):
    print(i)

from itertools import combinations
players=["John","Jani","Janardhan"]
for i in combinations(players,1):
    print(i)
    
from itertools import combinations
players=["John","Jani","Janardhan"]
for i in combinations(players,3):
    print(i)

from itertools import combinations
number=[0,1,2,3]
for i in combinations(number,2):
    print(i)

################################################################
#permutations()
from itertools import permutations
players=["John","Jani","Janardhan"]
for seat in permutations(players,2):
    print(seat)
    
from itertools import permutations
number=[0,1,2,3]
for i in permutations(number,2):
    print(i)
    
from itertools import permutations
number=[0,1,2,3]
for i in permutations(number,1):
    print(i)

from itertools import permutations
number=[0,1,2,3]
for i in permutations(number,3):
    print(i)

################################################################
#product
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['Virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)

from itertools import product
a=[0,1,2,3]
b=[0,1,2,3]
for i in product(a,b):
    print(i)

from itertools import product
a=[0,1,2,3]
b=[0,1,2,3]
c=[0,1,2,3]
for i in product(a,b,c):
    print(i)

################################################################
#filter()
age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])

################################################################
'''In python, assignment statement (obj_b=obj_a)
do not create real copies.
It only creates a new variable with the same reference. So 
when you want to make actual copies of mutual objects(lists,dicts)
and want to modify the copy without affecting the original, u 
have to be careful.

For nested objects: shallow copy and deep copy

Shallow copies --> Only one level deep. It creates a new 
collection and populates it with references to the nested object

Deep copies --> A full independent clone. It creates a new 
collection and then recursively populates it with the copies of 
the nested objects.'''
#Assignment operation
#This will only create a new variable with the same reference.
list_a=[1,2,3,4,5]
list_b=list_a        # new reference is created

print(list_a)
print(list_b)

list_a[0]=-10
print(list_a)
print(list_b)





    

    