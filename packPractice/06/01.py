"""
生成邀请码
"""

import random, string
import time

def ran_str(num, length=5):
    for i in range(num):
        Chars = string.ascii_letters + string.digits
        charList = [random.choice(Chars) for i in range(length)]
        charStr = ''.join(charList)
        # print(type(charStr))
        yield charStr
# print(ran_str(20))
yie_str = ran_str(20)
print(yie_str.__next__())
# for i in yie_str:
#     print(i)
print(time.time())