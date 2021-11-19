# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import struct 

version = struct.calcsize("P")*8

print("Python shell is in", version,"bits")