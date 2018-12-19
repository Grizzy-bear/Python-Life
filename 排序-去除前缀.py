import os
import re
import sys

# BASEDIR = ""

def filename(file_dir):
    i = 1
    for root, dir, files in os.walk(file_dir):
        print(root)
        print(dir)
        # print(files)
        for file in files:
            old_name = file
            old_path = os.path.join(root, old_name)
            # print(old_name)
            print(old_path)
            listG = list(old_name)[6:]
            # print(listG)
            newName = ''.join(listG)
            # print(newName)
            newPath = os.path.join(root, newName)
            # print(newPath)
            os.rename(old_path, newPath)

filename("D:/user/Desktop/童林传/")