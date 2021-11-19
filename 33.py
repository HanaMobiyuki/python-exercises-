# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def weird_sum(a, b, c):
    if((a == b) or (a == c) or (b == c)):
        return 0
    else:
        return int(a+b+c)
print(weird_sum(1, 2, 3))
print(weird_sum(2, 2, 3))