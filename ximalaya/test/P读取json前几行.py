# conding = utf-8

import json

with open("../GWDJson/GWD01.json") as f:
    JsonContent = json.load(f)
    # print(JsonContent["data"]["tracksAudioPlay"][0]["index"])
        
    # JsonContent["data"]["trddacksAudioPlay"][0]["trackName"]
    content = JsonContent["data"]["tracksAudioPlay"][0]
    for item in content:
        print(item[0])

