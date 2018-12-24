import itchat
import time
from itchat.content import TEXT
import csv

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

# 写入到CSV
# csvFile = open('csvData.csv','a')
# writer = csv.writer(csvFile)
# writer.writerow(['名字','显示名字','性别','身高','地点','签名','头像'])

# csvFile.close()

# def get_stature(name):
#     pass

# for i in range(total):
#     name = memberList['MemberList'][i]["NickName"]
#     displayname = memberList['MemberList'][i]['DisplayName']
#     sex = memberList['MemberList'][i]['Sex']
#     stature = get_stature(displayname)
#     location = 

print(memberList['MemberList'][i])

#     if memberList['MemberList'][i]['Sex'] == 2:
#         female += 1
#         print(memberList['MemberList'][i]['DisplayName'], memberList['MemberList']
#               [i]["NickName"], memberList['MemberList'][i]['Signature'], sep='******')
#     elif memberList['MemberList'][i]['Sex'] == 1:
#         male += 1
#         print(memberList['MemberList'][i]['DisplayName'], memberList['MemberList']
#               [i]["NickName"], memberList['MemberList'][i]['Signature'], sep='******')
#     else:
#         print("性别不详")

# print("男生有%s人" % (male))
# print("女人%s人"%(female))

