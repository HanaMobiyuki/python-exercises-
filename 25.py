# Write a Python program to check whether a specified value is contained in a group of values. 
def value_check(lst,n):
    check = "False"
    for x in range(len(lst)):
        if lst[x] == n:
            return True
    return False
print(value_check([1,2,3,5,6],6))
print(value_check([1,2,3,5,6,],4))