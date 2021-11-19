# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

from math import sqrt

def distance(a1, a2, b1, b2):
    dist = sqrt(((a1-b1)*(a1-b1))+((a2-b2)*(a2-b2)))
    return dist
print(distance(1, 2, 5, 5))