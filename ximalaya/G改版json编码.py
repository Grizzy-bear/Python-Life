import json

with open('GWD01.json',"r") as load_f:
    load_content = json.load(load_f)
print(load_content)
