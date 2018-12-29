import re
import jieba

s = "(西安-襄阳) 182 大鼠 32"
# s = "20岁的可爱小管理"
# print(list(s))

# b = re.sub("\s", " ", s)
# b = re.findall("\w", s)

# 过滤其他字符，只留下汉字
m = re.sub("[\!\%\[\]\,\。\()\-\~]", " ", s)
'''  
提取数字
'''
num = re.sub("\D", " ", m)
''' 
提取文字
'''
b = re.sub("\d", " ", m)
# print(b.strip())
# print(b.lstrip())
# print(list(b.strip()))
c = b.strip()
newlist = []

new = jieba.__lcut(c)
# print(type(new))
print(new)
"""  
不可使用for循环删除空格，如果尾向也是空格则无法删除
需使用：
1， while '' in test:
        test.remove('')
2, mytest = [i for i in test if i != '']
"""
# mytest = [i for i in new if i != ' ']
# print(mytest)

for i in new:
    if i != ' ':
        newlist.append(i)
print(newlist)

# print(b.rstrip())
