import re

s = "182 的身份 32"
# print(list(s))

# b = re.sub("\s", " ", s)
# b = re.findall("\w", s)
b = re.split("\w", s)
print(b)
