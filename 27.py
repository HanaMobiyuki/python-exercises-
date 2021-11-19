# Write a Python program to concatenate all elements in a list into a string and return it.
def listtostr(list):
    string = str(''.join(map(str, list)))
    return(string)
print(listtostr([1, 2, 3, 4, 'a', 'b', 6]))