import random

Lower = "abcdefghijklmnopqrstuvwxyz"
# bG = "AbcDfGijKnMnopqrStuvvxYZ"
# print(Lower.upper())
seq = ("1","2","4")
Upp = Lower.upper()+Lower
print(Upp)
# print(type(Upp))
Dict={"a":"y"}
for i in Lower:
    if i in Dict:
        continue
    else:
        value = random.choice(Upp)
        Dict2 = {i:value}
        Dict.update(Dict2)
    # print(i)
    # Dicto{i:random.choice(Upp)}

print(Dict)