"""
使用redis案例
"""
import redis
import sys
import time
from faker import Faker
import random

f = Faker(locale="zh_CN")
f.seed(4321)

a = 1

# 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
r = redis.Redis(host='127.0.0.1', port=6379, password=123456, decode_responses=True)

# r.set('name','jux')
# print(r['name'])

for i in range(10):
    jus = f.name()
    r.sadd("Invited",jus)

print(r.smembers("Invited"))
