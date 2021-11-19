#  Write a Python program to get the least common multiple (LCM) of two positive integers.

def LCM(a, b):
    if a > b:
        bigger = a
    else:
        bigger = b
    while(True):
        if((bigger % a == 0) and (bigger %b == 0)):
            lcm = bigger
            break
        bigger = bigger + 1
    return lcm
print(LCM(13, 450))
print(LCM(75, 123))