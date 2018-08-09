"""
import random

s=[]
def Dec_random(x):
    
    my_list=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for i in range(x):
        s.append(random.choice(my_list))
    J="".join(s)
    return "0x"+str(J)
        
"""

from random import randint
def dec_random(x):
    s = []
    for i in range(x):
        # https://ascii.cl/
        s.append(chr(randint(48,57) if randint(1,2)%2==0 else randint(65,70)))
    return "0x"+"".join(s)

a=int(input())
print(dec_random(a))

