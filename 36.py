# Write a Python program to add two objects if both objects are an integer type.

def addifint(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Items are not both ints"
    else:
        return a+b
print(addifint(12, 13))
print(addifint('a', 12))
print(addifint([1,2,3], 25))