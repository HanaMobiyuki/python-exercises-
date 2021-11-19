# Write a Python program to test whether a number is within 100 of 1000 or 2000.
# you said : i assume you have to check if it's like, in the range (900-1100) + (1900-2100)

number = int(input("Enter a number : "))
if 900 <= number <= 1100:
    print("Number is withing 100 of 1000")
elif 1900 <= number <= 2100:
    print("Number is withing 100 of 2000")
else:
    print("Number isn't within 100 of 1000 or 2000")