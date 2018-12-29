"""
生成虚假信息方便注入到数据库
"""
# import faker
from faker import Faker
from faker import Factory
import random

f = Faker(locale="zh_CN")
f.seed(4321)
print(f.name())
print(f.name())
# f.provider()
# print(f.name())

print(str(f.safe_email()))
# for i in range(1,10):
    # print(f.name()+ " " + str(f.date()) +" " +f.safe_email()+" "+f.phone_number())

# print(faker.random())
# fake = Factory('zh_CN')
# fake.name()
