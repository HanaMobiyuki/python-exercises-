# Write a Python program to check whether a file exists.

from os.path import isfile

def checkFile(filename):
    if isfile('./'+filename) == True:
        return "The file exists"
    else:
        return "The file doesn't exist"
print(checkFile('girlboss.sex'))
print(checkFile('41.py'))