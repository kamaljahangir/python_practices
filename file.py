#! /usr/bin/python3

import sys

data=sys.argv[1:]
# file creation
for i in data:
	f=open("a.txt",'w')
	f.write(i)
	f.write("\n")
	
	f.close()
	
# Reading File
	f=open("a.txt",'r')
	f.read(i)
	f.read("\n")
	
	f.close()

# File Read and Write

