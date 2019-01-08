import ijson
import os
import re
from pandas.io.json import json_normalize
import json

BASEDIR = os.getcwd() + '\pactice\Python-Life\Python-Life\StatisticsWechat\city.json'
out = re.sub(r'\\','/',BASEDIR)

f1 = open(out, 'rb')
content = f1.read()
f1.close()
# print(content)
text = json.loads(content)
new = json_normalize(text)
print(new)

# with open(out, 'rb') as f:
#     objects = ijson.items(f, 'city')
#     columns = list(objects)

# print(columns)