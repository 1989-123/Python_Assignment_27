# Write a python script to implement try except and else block for division


try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
except ZeroDivisionError:
    print("Can't divisible by zero")
except ValueError:
    print("Enter number only...")
else:
    print(x // y)
finally:
    print("File closed")
    