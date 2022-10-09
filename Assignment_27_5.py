# Write a python script to handle multiple Exception in one try


try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(x // y)
except ZeroDivisionError:
    print("Can't divisible by Zero")
except ValueError:
    print("Enter number only...")
