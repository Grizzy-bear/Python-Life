"""
SQLAlchemy操控数据库
"""

# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from random import randint
from sqlalchemy import ForeignKey


DB_CONNECT = "mysql+pymysql://test:1234@127.0.0.1/Students"
engine = create_engine(DB_CONNECT, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

BaseModel = declarative_base()

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all()

class Stu(BaseModel):
    __tablename__ = 'stu'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30))

class Cla(BaseModel):
    __tablename__ = 'cla'
    id = Column(Integer, primary_key=True)
    cname = Column(CHAR(30))

class Grade(BaseModel):
    __tablename__ = 'grade'
    uid = Column(Integer, ForeignKey('stu.id'))
    cid = Column(Integer, ForeignKey('cla.id'))
    id = Column(Integer, primary_key=True)
    gre = Column(Integer)


