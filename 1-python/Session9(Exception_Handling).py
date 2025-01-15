

###########Exception Handling
'''Sometimes a single piece of code might be suspectedd to have
 more then one tye of error for handling such situation we 
 can have multiple except blocks for a single try block'''

try:
    num=50
    denom=int(input("Enter the denom:"))
    print(num/denom)
    print("Div performed successfully")
except ZeroDivisionError:
    print("Denom as zero is not allowed")
except ValueError:
    print("Only integers should be entered")
    
    
try:
    num=50
    denom=int(input("Enter the denom:"))
    print(num/denom)
    print("Div performed successfully")
except ValueError:
    print("Only integers should be entered")
except :
    print("OOPS....some exception raised")  
    
    
###Exception handling with try...except and else
try:
    num=50
    denom=int(input("Enter the denom:"))
    quo=num/denom
    print("Div performed successfully")
except ZeroDivisionError:
    print("Denom as zero is not allowed")
except ValueError:
    print("Only integers should be entered")
else:
    print("The result is",quo)

###Exception handling with try...except..else and finally
try:
    num=50
    denom=int(input("Enter the denom:"))
    quo=num/denom
    print("Div performed successfully")
except ZeroDivisionError:
    print("Denom as zero is not allowed")
except ValueError:
    print("Only integers should be entered")
else:
    print("The result is",quo)
finally:
    print("Over and out")