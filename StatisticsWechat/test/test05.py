import os
import sys

BASEDIR = os.path.split(os.path.realpath(__file__))[0]
f1 = os.path.realpath(__file__)
f2 = os.path.dirname(os.path.realpath(__file__))
f3 = os.path.split(os.path.realpath(__file__))
f4 = os.path.abspath(__file__)
f5 = os.getcwd()
f6 = sys.argv[0]
f7 = sys.path[0]

print(BASEDIR)
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)
print(f6)
print(f7)

""" 
f:\1AFILE\programming\python\pactice\Python-Life\Python-Life\StatisticsWechat\test
f:\1AFILE\programming\python\pactice\Python-Life\Python-Life\StatisticsWechat\test\test05.py
f:\1AFILE\programming\python\pactice\Python-Life\Python-Life\StatisticsWechat\test
('f:\\1AFILE\\programming\\python\\pactice\\Python-Life\\Python-Life\\StatisticsWechat\\test', 'test05.py')
f:\1AFILE\programming\python\pactice\Python-Life\Python-Life\StatisticsWechat\test\test05.py
F:\1AFILE\programming\python
f:\1AFILE\programming\python\pactice\Python-Life\Python-Life\StatisticsWechat\test\test05.py
f:\1AFILE\programming\python\pactice\Python-Life\Python-Life\StatisticsWechat\test

 """