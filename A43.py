"""
import re
def regx(s):
    return re.search('9$' , str(s))

def func(y):
    s = list(filter(lambda x:regx(x**2),y))
    return s
    
"""

def func(y):
    return list(filter(lambda x:str(x**2)[-1]=='9',y))

x=[1,2,3,7,8,9,13,17,37,41]
print(func(x))
