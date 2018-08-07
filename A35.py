"""
def common(x,y):
    L=[]
    L=set(x)&set(y)
    return L
    
"""
def common(x,y):
    return list(set(x)&set(y))

a=[1,2,3]
b=[1,2]
c=["あ","い","う"]
d=["あ","い"]
print(common(a,b))
print(common(c,d))
