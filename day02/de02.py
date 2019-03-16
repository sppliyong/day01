if __name__ == '__main__':
    nset={1,2,3,3,4,4,4}
    mset={7,8,9,3}
    gset=nset|mset
    print(gset)#或运算是并的意思
    aset=nset&mset
    print(aset)
    bset=nset-mset
    print(bset)
    cset=mset-nset
    print(cset)
    dset=mset^nset
    print("dset={0}".format(dset))
    mmax=max(nset)
    print("mmax={0}".format(mmax))
    mset.update({1,1,1,10,1})
    print(mset)
    pset=mset.copy()
    print("pset:{0}".format(pset))
    mset.remove(1)
    print(mset)
    mset.discard(100)
    vset= frozenset(mset)
    print(vset)
