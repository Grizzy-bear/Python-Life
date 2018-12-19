import json
import requests
import time
import os
from bs4 import BeautifulSoup

url = "https://www.kuaidaili.com/free/"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}

def get_proxy_datas():
    html = requests.get(url, headers=headers)
    content = html.content
    soup = BeautifulSoup(content, 'lxml')
    ips = soup.find_all('td', attrs={'data-title':'IP'})
    ports = soup.find_all('td', attrs={'data-title':'PORT'}) 
    print("开始写入代理ip和端口......")
    write_conf(ips, ports)
    print("代理写入完成")

def write_conf(ips, ports):
    for i in range(0, len(ips)):
        print("----> IP:"+ips[i].string+"PORT:" + ports[i].string+"------>")
        time.sleep(1)
        with open('~/Desktop/proxy.conf','a+') as f:
            f.write('http %s  %s\n'%(ips[i].string, ports[i].string))

get_proxy_datas()
