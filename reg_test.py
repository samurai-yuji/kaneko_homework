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
print()

for m in re.finditer("[0-9]","a1b20c300"):
    print(m.group())

print(re.findall("[0-9]","a1b20c300"))

for m in re.finditer("[0-9]*","a1b20c300"):
    print(m.group())

print(re.findall("[0-9]*","a1b20c300"))

for m in re.finditer("[^0-9]","a1b20c300"):
    print(m.group())

print(re.findall("[^0-9]","a1b20c300"))

#####
print()

print("Matched.") if re.search("^ab?$","a") else print("Not matched...")
print("Matched.") if re.search("^ab?$","b") else print("Not matched...")
print()
print("Matched.") if re.search("^ab{1,3}?$","a") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}?$","ab") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}?$","abb") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}?$","abbb") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}?$","abbbb") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}?$","abbbbb") else print("Not matched...")
print()
print("Matched.") if re.search("^ab{1,3}$","a") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}$","ab") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}$","abb") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}$","abbb") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}$","abbbb") else print("Not matched...")
print("Matched.") if re.search("^ab{1,3}$","abbbbb") else print("Not matched...")

#####
print()

try:
    s = re.search("a(b)c","abc")
    print(s.group())
    print(s.group(1))
except IndexError as e:
    print("Error! {0}".format(e))

print()
try:
    s = re.search("abc","abc")
    print(s.group())
    print(s.group(1))
except IndexError as e:
    print("Error! {0}".format(e))

#####
print()

for m in re.finditer("\d+|\d+\.\d*","10a 20.1b 30.1c a40."):
    print(m.group())

print()
for m in re.finditer("\d+\.*\d*","10a 20.1b 30.1c a40."):
    print(m.group())

print()
for m in re.finditer("\d[.\d]*","10a 20.1b 30.1c a40."):
    print(m.group())

print()
for m in re.finditer("\d+\.\d*|\d+","10a 20.1b 30.1c a40."):
    print(m.group())

#####
print()

print(float("100.0"))
print(float("100."))
