"""
Write a python script to create a calculator with 
4 basic operations, and handle a maximum number of exceptions. 
"""

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    if y == 0:
        raise ZeroDivisionError()
    elif x == str or y == str:
        raise ValueError()
    else:
        raise Exception()
    print(x + y)
    print(x - y)
    print(x * y)
    print(x // y)
except ZeroDivisionError:
    print("Can't divisible by zero")
except ValueError:
    print("Enter number only...")
except SyntaxError:
    print("Enter valid syntax...")
except TypeError:
    print("Enter valid type...")
