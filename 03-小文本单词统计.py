# 统计小文本内单词的数量

import os
from collections import Counter
import fileinput
import string
import re

BASE_DIR = os.getcwd() + '/practice/python/dailyPro/05/'

filePath = BASE_DIR + '04.txt'
# print(filePath)

with open(filePath) as f:
    content = f.read(500)
    f.close()

pattern = re.compile(r'\W')

contentS = re.sub(pattern, ' ', content)

# print(contentS)

list_content = contentS.split(' ')

# print(list_content)
cnt = Counter()

for word in list_content:
    cnt[word] += 1
cnt = dict(cnt)

for key, value in cnt.items():
    print(key+":"+str(value))