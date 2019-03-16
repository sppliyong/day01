import  random
if __name__ == '__main__':
    mlist=[random.randint(1,100) for i in range(1,11)]
    aset=set(mlist)
    nlist=[random.randint(1,100) for i in range(1,11)]
    bset = set(nlist)
    cset=aset|bset
    qlist=list(cset)
    print(qlist)
    