from functools import reduce

a = [1,2,3,4,5]
print(a)

b = map(lambda x: x*2, a)
print(type(b))
print(list(b))

b = [ x*2 for x in a ]
print(type(b))
print(b)

b = filter(lambda x: x%2 == 0, a)
print(type(b))
print(list(b))

b = reduce(lambda x,y: x+y, a)
print(type(b))
print(b)

c = {"k1":10, "k2":20, "k3":30}
d = dict([ (x,y*2) for x,y in c.items() ])
print(type(d))
print(d)

