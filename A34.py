"""
def delete_word(a):
    L=[]
    moji=0
    for i in a:
        L.append(i)
    F=L.count("-")
    for j in range(F):
        L.remove("-")
    moji="".join(L)
    return moji
"""
    
def delete_word(a):
    return "".join(a.split("-"))

print(delete_word("a-b-c"))
