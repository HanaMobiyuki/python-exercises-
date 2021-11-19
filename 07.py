# Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Enter file name : ")
filenamelist = filename.split(".")
print(filenamelist[1])