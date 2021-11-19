#  Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sum20(a, b):
    if((a+b>=15) and (a+b<=20)):
        return 20
    else:
        return int(a+b)
print(sum20(5, 9))
print(sum20(10, 9))