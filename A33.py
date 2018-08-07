"""
def chain_word(a):
    L=[]
    moji=0
    for i in a:
        L.append(i)
    moji='-'.join(L)
    return moji
"""
def chain_word(a):
    return "-".join(a)
    
print(chain_word("abc"))
