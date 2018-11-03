import os


BASEDIR = os.path.split(os.path.realpath(__file__))[0]
temp = []
# print(BASEDIR)
def filename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root, dirs, files)
        for File in files:
            temp.append("- " +File+"\n")
    print("ok")
        # print(temp)
    return temp

content = filename(BASEDIR)
print(content)
# with open('try.txt','w') as f:
#     # f.writelines(filename(BASEDIR))
#     f.writelines(content)
path = BASEDIR + "/try.txt"
print(path)
foo = open(path,"w",encoding="utf-8")
foo.writelines(content)
foo.close()
# foo.flush()

# filename(BASEDIR)