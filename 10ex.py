# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Homework from Laura: make this same program, make it so it so it only accepts numerical values between 0 and 9. If the input is something that is not in that range, make the program ask for a proper input instead of crashing.
n = input("Input an int : ")
if n != int or (n < 0 or n > 9):
    print("Please enter a number between 0 and 9")
else:
    n1 = int("%s" % n)
    n2 = int("%s%s" % (n,n))
    n3 = int("%s%s%s" % (n,n,n))
    sum = n1+n2+n3

    print("n = ", n1)
    print("nn = ", n2)
    print("nnn = ", n3)
    print("n+nn+nnn = ", sum)