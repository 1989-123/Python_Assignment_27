# Write a python script to create a ValueError

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(x + y)
except ValueError:
    print("Enter a number bola tha.. Gadhe...")
finally:
    print("Kuch to gadbad he daya")
