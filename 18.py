# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
def sum_triple(a, b, c):
    s = a + b + c
    if a == b == c:
        s = s * 3
    return s
print(sum_triple(1, 2, 3))
print(sum_triple(3, 3, 3))