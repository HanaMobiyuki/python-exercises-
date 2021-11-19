# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

seq = input("Enter sequence of numbers seperated with commas : ")
my_list = seq.split(",")
my_tuple = tuple(my_list)
print('List : ',my_list)
print('Tuple : ',my_tuple)
