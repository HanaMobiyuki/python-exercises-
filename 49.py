from os import listdir
from os.path import isfile, join
file_list = [x for x in listdir() if isfile(join(x))]
print(file_list)