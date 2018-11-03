'''
#@Author: Grizlly 
# @Date: 2018-04-05 18:30:52 
# -*- coding: utf-8 -*- 
'''
import requests
from bs4 import BeautifulSoup
import os
import datetime

dt = datetime.datetime.now()
cd = str(dt.year) + '0' + str(dt.month) + '0'+str(dt.day)
print(cd)
# os.mkdir(r'E:\\Pictures\\Bings', exit_ok=True)
def mkdirs(path):
    # if path is not exit
    if not os.path.exists(path):
        os.mkdir(path)
        print('create dir')
        return True
    else:
        print('存在')
        return False

# print('ok')
path = 'E:/Pictures/Bings'
mkdirs(path)

url = 'http://bingwallpaper.com/'
sc = requests.get(url)
# print(sc.text)
soup = BeautifulSoup(sc.text, 'lxml')
image = soup.select('#photos > div:nth-of-type(1) > a > img')
# image = soup.xpath('//*[@id="photos"]/div[1]/a/img')
# print(type(image))
for imag in image:
    # print(imag['src'])
    image_url = imag['src']
    res = requests.get(image_url)
    # print(path)
    # path = os.path.expanduser(path)
    Dirname = path +'/'+ cd+'.jpg'
    print(Dirname)
    with open(Dirname, 'wb') as file:
        file.write(res.content)
        print('成功')
# os.system('gsettings set org.gnome.desktop.background picture-uri http://file:///home/radioactive/Bing/'+cd+'.jpg')
#os.system(gsettings set org.mate.background picture-filename Dirname)


