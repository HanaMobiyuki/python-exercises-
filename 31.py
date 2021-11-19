#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(a, b):
    gcd = 1
    if a % b == 0:
        return b
    for x in range(int(b*0.5), 0, -1):
        if a % x == 0 and b % x == 0:
            gcd = x
            break
    return gcd
print(gcd(23, 4))
print(gcd(400, 100))
print(gcd(3, 9))