# Write a Python program to count the number 4 in a given list.
def list_count_4(number_list):
    count = 0
    for x in range(len(number_list)):
        if number_list[x] == 4:
            count = count + 1
    return count
print(list_count_4([1, 4, 2, 4, 3, 4, 4, 5, 4]))
print(list_count_4([4,1,4,1,2,7,1,2,3,4]))