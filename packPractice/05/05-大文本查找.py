import os
# import flashtext
from flashtext import KeywordProcessor
import fileinput

kp = KeywordProcessor()

kp.add_keyword('另外','现在')
kp.add_keyword("第二部分","第三部分")
# print(os.path.abspath('.')
# print(os.path.abspath(os.path.dirname(__file__)))
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

print(BASE_DIR)
# for i in os.listdir(BASE_DIR):
#     print(i)
#     if i == "06.txt":
        # j = kp.replace_keywords(i)
i = BASE_DIR +'/06.txt'
for line in fileinput.input(i):
    j = kp.replace_keywords(line)
    print(j)