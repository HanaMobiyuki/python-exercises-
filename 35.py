# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def equal_int(a, b):
    if (a==b) or abs(a-b)==5 or (a+b)==5:
        return True
    else:
        return False
print(equal_int(1, 6))
print(equal_int(2, 3))
print(equal_int(9, 4))
print(equal_int(15, 10))
print(equal_int(10, 10))
print(equal_int(10, 11))