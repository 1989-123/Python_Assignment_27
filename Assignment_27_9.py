# Write a python script to raise a ValueError.

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    if x == str or y == str:
        raise ValueError()
except ZeroDivisionError:
    print("Can't divisible by zero")
except ValueError:
    print("Enter number only...")
else:
    print(x // y)
finally:
    print("File closed")
