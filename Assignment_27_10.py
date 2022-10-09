# Write a python script to implemented a nested Try Except block

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))

except ValueError:
    print("Enter number only...")
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
    except ZeroDivisionError:
        print("Can't divisible by zero")
finally:
    print("File closed")
    