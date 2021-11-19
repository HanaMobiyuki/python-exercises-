# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def add_string(str, n):
    new_str = ''
    for x in range(n):
        new_str = new_str + str
    return(new_str)
print(add_string("test", 4))
print(add_string("sex", 6))