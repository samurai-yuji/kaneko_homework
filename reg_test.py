import re

m = re.search("a","aabaa")
print(type(m))
print(m.group())

m = re.findall("a","aabaa")
print(type(m))
print(m)

for m in re.finditer("a","aabaa"):
    print(type(m))
    print(m.group())

#####

for m in re.finditer("[0-9]","a1b20c300"):
    print(m.group())

for m in re.finditer("[0-9]*","a1b20c300"):
    print(m.group())

print(re.findall("[0-9]*","a1b20c300"))

