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

"""  
                                                city    name
0  [{'name': '北京市', 'area': ['东城区', '西城区', '朝阳区',...     北京市
1  [{'name': '天津市', 'area': ['和平区', '河东区', '河西区',...     天津市
2  [{'name': '石家庄市', 'area': ['长安区', '桥西区', '新华区'...     河北省
3  [{'name': '太原市', 'area': ['小店区', '迎泽区', '杏花岭区'...     山西省
4  [{'name': '呼和浩特市', 'area': ['新城区', '回民区', '玉泉区...  内蒙古自治区
"""
# print(df.loc[])
# print(df.head())

name = df.loc[:,'name']


for i in name:
    if i == "北京市":
        print("ok")
    else:
        continue

city = df.loc[:,'name']
print(city)
# for j in city:
#     # print(j)
#     if j == None:
#         continue
#     newcity = json_normalize(j)
#     print(newcity)
# print(type(city))

# print(type(content))

# """ 
# 处理json文件

#  """
