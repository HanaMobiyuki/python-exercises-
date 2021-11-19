# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def new_string(string):
    list_str = list(string)
    if list_str[0] == 'I' and list_str[1] == 's':
        return string
    else:
        new_list = ['I', 's', ' '] + list_str
        new_str = str(''.join(map(str, new_list)))
        return new_str
print(new_string("Is Boss"))
print(new_string("Girl"))