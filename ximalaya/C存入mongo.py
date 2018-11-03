import json
import pymongo

clients = pymongo.MongoClient()
db = clients["GDGxiang"]
tableJson = db["GDGJson"]


for i in range(1, 7):
    with open("./GWDJson/GWD0{}.json".format(i)) as Json_f:
        Json_content = json.load(Json_f)
        testName = Json_content["data"]["tracksAudioPlay"][0]["trackName"]
       #  whetherJsonNum = tableJson.find({"{}".format(testName): None}).count()
        
        if tableJson.find({"{}".format(testName): None}):
        # if whetherJsonNum >= 1: 
               tableJson.insert(Json_content)
               print("插入成功!!!!")
        else:
            print("已经下载！！！")
            
