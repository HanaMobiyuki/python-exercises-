# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
def first_2_copy(str, n):
    minlen = 2
    if len(str) < minlen:
        minlen = len(str)
    first_2 = str[:minlen]
    new_str = ''
    for x in range(n):
        new_str = new_str + first_2
    return new_str
print(first_2_copy("Girl boss", 2))
print(first_2_copy("Pi", 2))
print(first_2_copy("a", 5))