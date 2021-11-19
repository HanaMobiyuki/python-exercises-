# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(input("Input and int : "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))
print(n1+n2+n3)