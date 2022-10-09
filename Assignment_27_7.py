# Write a python script to add a finally block for the above script

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    if y == 0:
        raise ZeroDivisionError()
    elif x == str or y == str:
        raise ValueError()
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
finally:
    Exception