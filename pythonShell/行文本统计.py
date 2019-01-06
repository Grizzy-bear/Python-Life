# 统计文字的出现频率

import os
from collections import Counter
import fileinput

sumData = []
# print(os.getcwd())
BASE_DIR = os.getcwd() + '/practice/python/dailyPro/05/'

# 大文件读取
# for line in fileinput.input(BASE_DIR+'02.txt'):
#     print(line)


# print(BASE_DIR)
for name in os.listdir(BASE_DIR):
    if name.endswith('.txt'):
        print(name,"?")
        # print()
        filePath = BASE_DIR+name
        with open(filePath,'r') as f:
            data = f.readlines()
            f.close()
        sumData += [line.strip() for line in data]
print("okkok")

cnt = Counter()
print(sumData)

for word in sumData:
    cnt[word] += 1
cnt = dict(cnt)

for key, value in cnt.items():
    print(key+":"+str(value))
    
