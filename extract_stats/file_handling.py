#!/usr/bin/python
import sys
import os

dir_ = sys.argv[1]
file_ = sys.argv[2]

file_path = os.path.join(dir_, file_)

try:
    file_ = open(file_path, "w+")
    file_.write("hello world \n how are you doing?")
    file_.close()
except IOError:
    print("Could not open file for writing")

try:
    file2_ = open(str(file_path), "r")
    str = file2_.read()
    print(str)
    file2_.close()
except IOError:
    print("could not open the file for reading")


