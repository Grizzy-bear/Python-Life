import json
import demjson
import ast
import os
import re
from pandas.io.json import json_normalize
import pandas as pd

aa = "北京"
bb = "男"

print(len(aa))
print(len(bb))

# print(os.getcwd())
BASEDIR = os.getcwd() + '\pactice\Python-Life\Python-Life\StatisticsWechat\city.json'

# out = re.sub(r'\', '/', s)
out = re.sub(r'\\','/',BASEDIR)
# print(out)
# out = re.sub(r'/', '\\\\',out1)
# print(out)
# BASEDIR.replace('\','/')
# print(BASEDIR)
# # jsonFile = './city.json'
# dealJson = demjson.decode(out)
# dealJson = ast.literal_eval(out)

# # province = json.load(jsonFile)
# print(dealJson)


f1 = open(out, 'rb')
content = f1.read()
f1.close()
# print(content)
text = json.loads(content)
new = json_normalize(text)
# print(new)
df = pd.DataFrame(new)
# print(df.columns)
# print(df[df['city'.isin]])

print(df.loc[])

# print(type(content))

# """ 
# 处理json文件

#  """
