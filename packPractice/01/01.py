"""
从文本中筛选出8位长度的密码
"""


import os

def readfile(filePath, fileSize=1024*1024*100):
    # default 1024*1024 = 1M
    file_object = open(filePath)
    while True:
        chunk = file_object.readline()
        # chunk = file_object.read(fileSize)
        # if not chunk:
        #     break
        # yield chunk
        # return chunk
        # print(len(chunk))
        
        if len(chunk) == 8:
            print(chunk)
        else:
            continue

if __name__ == "__main__":
    file = "/home/lamplight/Desktop/douc"
    # for chunk in readfile(file):
    #     print(len(chunk))
    readfile(file)
