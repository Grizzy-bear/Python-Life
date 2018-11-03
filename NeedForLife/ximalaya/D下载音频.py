# import pymongo
import requests
import json
from urllib import request
import threading
import time

now = lambda: time.time()
#  for i in range(1,7):
#  with open("./GWDJson/GWD0{}.json".format(i)) as json_f:
#  JsonContent = json.load(json_f)
#  Name = JsonContent["data"]["tracksAudioPlay"][0]["trackName"]
#  Url = JsonContent["data"]["tracksAudioPlay"][0]["src"]
#  print("name:",Name,"url:",Url)
#  with open("./files/01.txt", "a") as f:
#  f.write(Name)
#  print("downloaded......")


def downloads(name, url):
    filename = "./files/" + name + ".m4a"
    request.urlretrieve(url, filename)
    print(name + " " + url + " " + "downloading..........")


threads = []
with open("./GWDJson/GWD01.json") as a, open("./GWDJson/GWD02.json") as b, open(
    "./GWDJson/GWD03.json"
) as c, open("./GWDJson/GWD04.json") as d, open("./GWDJson/GWD05.json") as d, open(
    "./GWDJson/GWD06.json"
) as e:
    start = now()
    for item in [a, b, c, d, e]:
        JsonContent = json.load(item)
        content = JsonContent["data"]["tracksAudioPlay"]
        for i in content:
            NewName = "GDG" + i["trackName"]
            Url = i["src"]
            print("add thread")
            t0 = threading.Thread(target=downloads(NewName, Url), args=(u"下载"))

            threads.append(t0)
    print(threads)
    for j in threads:
        j.setDaemon(True)
        j.start()
print("time:", now() - start)
