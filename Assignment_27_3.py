# Write a python script to handle the ArithmeticError

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(x // y)
except ZeroDivisionError:
    print("Can't divisible by Zero")
