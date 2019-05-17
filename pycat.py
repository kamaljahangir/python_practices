# /usr/bin/python3


import sys

file_name=sys.argv[1]

f=open(file_name)    # by default is read mode
for i in f:
	print(i)
