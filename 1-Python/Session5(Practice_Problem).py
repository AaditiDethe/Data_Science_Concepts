# Problem Solving: List, String

#Merging 2 dictionaries
dict1={"one":1,"two":2}
dict2={"three":3,"four":4}
dict3=dict1|dict2
dict3

'''write python code using logical operator and if elif
so as to check height as well as
so as to allow for roller coster aslo ask user age and check tickit accordingly'''
print("Welcome to the roller coaster")
height=int(input("Enter your height in cm:"))
if height>=120:
    print("Your eligible for roller coaster")
    age=int(input("Enter your age in years:"))
    bill=0
    if age<20:
        print("Child tickit is 5$")
        bill=5
    elif age>12 and age<18:
        print("young ticket is 35$")
        bill=10
    elif age>=45 and age<=55:
        print("Adult ticket is 35$")
        bill=30
    want_photo=input("Do you want photo Y or N :")
    if want_photo=='Y':
        bill+=3
        print(f"You need to pay {bill} in $")
    else:
        print(f"You need to pay {bill} in $")
else:
    print("Sorry your not eligible")
    
##################################################

height=float(input("Enter your height in m:"))
weight=float(input("Enter your weight in kg:"))
BMI=round((weight/(height*height)),2)
if BMI<18.5:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI<18.5 and BMI<25:
    print(f"You are normal weight and your BMI is:{BMI}")
elif BMI>25 and BMI<30:
    print(f"You are over weight and your BMI is:{BMI}")
elif BMI>30 and BMI<35:
    print(f"You are obese and your BMI is:{BMI}")
elif BMI>35:
    print(f"you are clinically obese and your BMI is:{BMI}")
    
##################################################

'''Write a program to find out is duplicate elelment from list'''

lst1=[1,2,3,4,5,6,6]
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        #compare current number with next number
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))


lst1=[6,1,2,3,4,5,6]
lst1.sort()
lst1
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        #compare current number with next number
        if(lst1[i]==lst1[i+1]):
            return True
    
    return False
print(is_duplicate(lst1))

################################################################
#Leap Year
def is_leap_year(year):
    if((year>0) and (year%4==0) or (year%400==0) and (year%100!=0) ):
        print("True")
    else:
        print("False")
#is_leap_year(2031)
is_leap_year(2024)

def is_leap_year(year):
    if((year>0) and (year%4==0) or (year%400==0) and (year%100!=0) ):
        return True
    else:
        return False
is_leap_year(2031)
is_leap_year(2000)

#################################################################
#Mario Pyramid
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()

#Diagonal path
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()

#Reverse diagonal path
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
'''if this print is not given then it will display '#' 
in all one single line'''

#HW diamond:

################################################################
#min() and max() function
'''min() --> gives minimum value
   max() --> gives maximum value'''

lst=[23,45,2,1,5,7,8,12]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("The min value",min)
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("Maximum value",max)
min_max(lst)

###########################################################
#Palindrome
def palindrome(inputstring):
    if inputstring=="":
        print("You entered wrong input")
    else:
        string=inputstring[::-1]
        if string==inputstring:
            print("The given string is palindrome.")
        else:
            print("Given string is not palindrome")
palindrome("wow")

def is_palindrome(input):
    if input=="":
        return "You entered wrong input."
    else:
        string=input[::-1]
        if string==input:
            return True
    return False
print(is_palindrome("steps on no pets"))
        
###########################################################
#
users=['admin','student','worker']
user=["admin","employee","student","teacher"]
for user in users:
    if user=='admin':
        print("Hello this is admin")
    elif user=='employee':
        print("Hello this is employee")
    elif user=='student':
        print("Hello this is student")
    elif user=='teacher':
        print("Hello this is teacher")
    else:
        print("Thank you")
#
role=["admin","employee","student","teacher"]
user=input("Enter your role:")
if user==role[0]:
    print("Hello this is admin")
elif user==role[1]:
    print("Hello this is employee")
elif user==role[2]:
    print("Hello this is student")
elif user==role[3]:
    print("Hello this is teacher")
else:
    print("Thank you")

###########################################################
#random()
import string
import random
'''pick the adjectives'''
adjectives=['sleepy','slow','smelly','wet','fat','orange',
            'yellow','green','blue','purple','fluffy',
            'white','proud','brave']

'''pick nouns'''
nouns=['apple','dinosaur','ball','toaster','goat','dragon',
       'hammer','duck','panda']
'''pick the words'''
import random
adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number=random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
#create the new secure password
password=adjective + noun + str(number) +special_char
print('your new password is:%s' %password)



#Another one?
#you can use a while loop to generate


