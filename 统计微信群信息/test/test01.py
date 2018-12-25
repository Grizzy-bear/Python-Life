import re
from cpca import *
# from getInfo import get_stature
import itchat

itchat.auto_login(enableCmdQR=False)
# itchat.auto_login(hotReload=True)
roomslist = []

name = "find soulmate"

def getroom_message(ChatName):
    # get room name
    # pass
    itchat.dump_login_status()
    RoomList = itchat.search_chatrooms(name=ChatName)
    if RoomList is None:
        print("没有%s群" % (ChatName))
    else:
        return RoomList[0]["UserName"]


memberList = itchat.update_chatroom(getroom_message(name), detailedMember=True)
total = len(memberList['MemberList'])
female = 0
male = 0

def get_stature(name):
    # pass
    """ 
    这部分的代码重新写，从名字里识别目前所在地名
    """

    Number = re.findall(r"\d+", name)
    if Number == []:
        age = 0
        stature = 0
        current_location = name
    elif len(Number) == 1:
        if Number[0] < 100:
            age = Number[0]
            stature = 0
        else:
            age = 0
            stature = Number[0]
    else:
        if Number[0] < 100:
            age = Number[0]
            stature = Number[1]
        else:
            age = Number[1]
            stature = Number[0]
    NumberData = [age, stature, current_location]
    return NumberData


data = get_stature(memberList['MemberList'][0]['DisplayName'])
print(data)