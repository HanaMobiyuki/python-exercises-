# Write a Python program to create a histogram from a given list of integers.

def histogram(int_list):
    for x in int_list:
        symbol = ''
        i = x
        while(i > 0):
            symbol += '*'
            i = i -1
        print(symbol)
histogram([9,2,4,3,6,1,1])