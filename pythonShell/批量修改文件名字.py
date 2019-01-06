import os
import sys
import re


def file_name(file_dir):
    i = 1
    # chdir(os.path.dirname())
    for root, dirs, files in os.walk(file_dir):
        print(root)
        # print(dirs)
        # print(files)
        # i = 1
        for file in files:
            # print(re.split(r'单田芳评书', file))
            old_name = file
            old_path = os.path.join(root, old_name)
            # new_name = file.split(r'单田芳评书')[1]
            # pattern = '\d\d'
            if i < 9:
                repl = '(' + '0' + str(i) + ')'
            else:
                repl = '(' + str(i) + ')'
            new_name = re.sub(r'\d{2}', repl, file)
            new_path = os.path.join(root,new_name)
            print(old_name + "-->" + new_name)
            os.rename(old_path, new_path)
            i += 1
            
            # print(type(file))


# file_name("C:\\Users\\Vencent\\Desktop\\单田芳评书大破冲霄楼")
file_name("/home/lamplight/Desktop/test")

