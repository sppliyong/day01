if __name__ == '__main__':
    mset=set()
    print(type(mset))
    nset={1,2}
    print(type(nset))
    mset={1,2,3,4,2,2,2}
    print(mset)
    if 1 in mset:
        print("存在")

    tset={"11","22","33",1,1,2}
    for i in tset:
        print("nset={0}".format(i))

    cset={(1,2,3),(4,5,6),(7,8,9)}
    for n,p,q in cset:
        print("nset = ",n,p,q)

    print("--------------")
    aaset={10,3,21,4,5,6,7,5,6}
    bbset={i for i in aaset if i%2==0 }
    print(bbset)

    print("***************")
    for i in aaset:
        print(i)

    print("")