import json
import demjson

aa = "北京"
bb = "男"

print(len(aa))
print(len(bb))

jsonFile = './city.json'
dealJson = demjson.decode(jsonFile)

# province = json.load(jsonFile)
print(dealJson[0]['name'][0])

""" 
处理json文件

 """