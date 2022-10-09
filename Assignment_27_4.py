# Write a python script to handle a ValueError

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(x + y)
except ValueError:
    print("Enter number only...")
