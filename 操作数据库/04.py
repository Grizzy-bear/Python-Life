"""
插入到mysql
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from random import randint
from sqlalchemy import ForeignKey
import datetime
import random, string
from faker import Faker
from faker import Factory
import time

t0 = time.time()

BaseModel = declarative_base()

DB_CONNECT = "mysql+pymysql://test:1234@127.0.0.1/Invited"
engine = create_engine(DB_CONNECT, echo=False)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

# fake data


def init_db():
    BaseModel.metadata.create_all(engine)

class Invit(BaseModel):
    __tablename__ = 'Invited'
    id = Column(Integer, primary_key=True, unique=True)
    Name = Column(CHAR(30))
    Phone = Column(VARCHAR(13))
    Invited = Column(VARCHAR(10))
    # Time = Column(Time, default=datatime.now, nullable=False)
    Date = Column(CHAR(50))
    Email = Column(VARCHAR(50))
    Address = Column(VARCHAR(50))


# yield 返回邀请码

def ran_str(num, length=7):
    for i in range(num):
        Chars = string.ascii_letters + string.digits
        charList = [random.choice(Chars) for i in range(length)]
        charStr = ''.join(charList)
        # print(type(charStr))
        yield charStr

# def insert_db(number=20, length=5):
#     yield_ran_str = ran_str(number)
#     for i in range(1,30):
#         Insert.id = i
#         Insert.Name = str(f.name())
#         Insert.Phone = int(f.phone_number())
#         Insert.Invited = str(yield_ran_str.__next__())
#         # Insert.Time = f.date()
#         Insert.Date = str(f.date())
#         Insert.Address = str(f.address())
#         Insert.email = str(f.safe_email())
#         print(f.safe_email())
#         session.add(Insert)
#         if i % 10 == 0 :
#             session.flush()
#         print("赋值成功!!!")
#     session.commit()
#     session.close()
#     t1 = time.time()
#     print("数据插入成功，时间是{}".format(t1-t0))



if __name__ == "__main__":
    init_db()

    f = Faker(locale="zh_CN")
    f.seed(4321)

    yield_ran_str = ran_str(20)

    Insert = [Invit(
        id = i,
        Name = str(f.name()),
        Phone = int(f.phone_number()),
        Invited = str(yield_ran_str.__next__()),
        Date = str(f.date()),
        Address = str(f.address()),
        Email = str(f.safe_email()),
    ) for i in range(20)]
    
    session.add_all(Insert)
    session.commit()
    session.close()
    print("成功")
    # insert_db(number=20)

