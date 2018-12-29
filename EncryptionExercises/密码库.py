import re

Lower = "abcdefghijklmnopqrstuvwxyz"
# etx = "abcdefg-1222"
atx = "3223234-wedsdd"
cont=""

# 替换功能
def rreplace(str2, old, new, *max):
    count = len(str2)
    if max and str(max[0]).isdigit():
        count = max[0]
    return new.join(str2.rsplit(old, count))


# print(rreplace(etx,'2','7',10))

# 第一规则
# if etx.find('a') is not None:
#     # print("oo")
#     cont = rreplace(etx,'a','7',10)
# # print(cont)
#     if etx.find('c') is not None:
#         cont =  rreplace(cont,'5','1',10)
# print(re.findall(r"\D",atx,re.I))
Dictionary = {
    'a': 'y',
    'b': 'y',
    'c': 'P',
    'd': 'a',
    'e': 'r',
    'f': 'A',
    'g': 'R',
    'h': 'V',
    'i': 'x',
    'j': 'n',
    'k': 'c',
    'l': 'o',
    'm': 'w',
    'n': 'Y',
    'o': 'U',
    'p': 'V',
    'q': 'J',
    'r': 'V',
    's': 'f',
    't': 'X',
    'u': 'a',
    'v': 'b',
    'w': 'O',
    'x': 'I',
    'y': 'S',
    'z': 'v'
}

# if etx.find()
cont = atx
for i in Lower:
    # print(i)
    if atx.find(i) is not None:
        cont2 =  rreplace(cont,'i',Dictionary['i'],10)
        cont = cont2
        print(cont)
        print("dd",cont2)
    else:
        # print(i)
        continue
# print(cont)
