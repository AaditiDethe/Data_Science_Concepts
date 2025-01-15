
'''Decorators are also called wrapper function'''
'''A python decorator is a function that takes in a function
and returns it by adding some functionality'''
def say_hi():
    return "hello moto"
def upper_case(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper
decorate=upper_case(say_hi)
decorate()

def string():
    return "hello world!!"
def upper_case(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper
de=upper_case(string)
de()
'''however python provides easier way to use decorators.
we simple use the @ symbol before the function we would
like to decorate'''

def upper_case(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper
@upper_case
def say_hi():
    return "hello moto"
say_hi()

'''we can use multiple decorators to a single function
however,the decorators will be applied in the order that
we have called them'''



def split_str(function):
    def wrapper():
        func=function()
        splited_str=func.split()
        return splited_str 
    return wrapper
def upper_case(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper
@split_str
@upper_case
def say_hi():
    return "hello moto"
say_hi()


#time calculation program
import time
def time_it(func):
    def wrapper(args,*kwargs):
        start=time.time()
        result=func(args,*kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took {total_time} mili sec")
        return result
    return wrapper
@time_it
def calc_sq(numbers):
    result=[]
    for number in numbers:        
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,1000000)
out_sq=calc_sq(array)
out_cube=calc_cube(array)
'''Debuging-->execution flow of program'''

#################################################################
#Modular programming
'''advantage-->reusability'''

#################################################################
#Exception
'''syntax errors - compilation errors
   semantic errors- leads to programs producing unexpected output
   runtime errors- most often lead to abnormal termination of 
                   programs or even cause the system to crash'''
'''Common Runtime error:
    1.Dividing number by zero
    2.Accessing an element that is out of bounds of an array.
     '''
'''Exception:
    An exception is a codition that is caused by a runtime error
      in the program
   8
    Types of Exception:
        1.Checked exception --> inability to acquire system resources
                       (inefficient memory,file does not exit)
        2.Unchecked exception --> occur because user entered wrong data
                           or failing to enter data at all'''
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)