# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
def diff(number):
    if number > 17:
        return(abs((number-17)*2))
    else:
        return(abs(number-17))
print(diff(23))
print(diff(11))