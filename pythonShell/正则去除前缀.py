import os
import re


def filename(BASEDIR):
    for root, dirs, files in os.walk(BASEDIR):
        # print(dirs)
        # print(files)
        for file in files:
            # print(file)
            # print(re.split('\-+', file))
            old_path = os.path.join(root, file)
            newName = re.split('\-+', file)[1]
            new_path = os.path.join(root, newName)

            print(newName)
            print(new_path)
            os.rename(old_path, new_path)


filename("/home/lamplight/Desktop/test/file")
