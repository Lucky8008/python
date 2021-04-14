"""
This is the program for adding two numbers
"""
import os,sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)
print("The content of file is:")
data=f.read()
print(data)